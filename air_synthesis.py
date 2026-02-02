"""
Prostorová syntéza kvality ovzduší České republiky (2020–2023)
Vytvoření typizace a regionalizace na základě imisních dat ČHMÚ
Grid 1×1 km, SRID 4258
"""

import geopandas as gpd
import pandas as pd
import numpy as np
from pathlib import Path
import re


# ============================================================================
# KONFIGURACE
# ============================================================================

# Cesty k datům
DATA_DIR = Path(r"C:\Skola\4_ZS\SYKAR\semestralka\V2\chmu_imise")
OUTPUT_DIR = Path.cwd() / "out"

# Vstupní soubory
INPUT_FILES = {
    2020: DATA_DIR / "chmu_imise_epsg4258_2020.gpkg",
    2021: DATA_DIR / "chmu_imise_epsg4258_2021.gpkg",
    2022: DATA_DIR / "chmu_imise_epsg4258_2022.gpkg",
    2023: DATA_DIR / "chmu_imise_epsg4258_2023.gpkg"
}

# Použití LVTV sloupců z ČHMÚ dat
# Data obsahují kategorie/intervaly, ne přesné koncentrace
# LVTV - oblasti s překročením imisních limitů BEZ zahrnutí O3 (0/1)
# LVTV_O3 - oblasti s překročením imisních limitů SE zahrnutím O3 (0/1)

# Volba hodnocení
USE_O3 = True  # True = použít LVTV_O3 (s ozónem), False = použít LVTV (bez ozónu)


# ============================================================================
# 1. NAČTENÍ A PŘEDZPRACOVÁNÍ DAT
# ============================================================================




def load_and_preprocess_year(file_path, year):
    """
    Načtení a předzpracování dat pro jeden rok
    Použití LVTV/LVTV_O3 sloupců jako indikátorů překročení
    """
    print(f"\nNačítám data pro rok {year}: {file_path}")
    
    if not file_path.exists():
        print(f"  VAROVÁNÍ: Soubor nenalezen!")
        return None
    
    gdf = gpd.read_file(file_path)
    print(f"  Načteno {len(gdf)} gridových buněk")
    
    # Přidání roku jako atributu
    gdf['rok'] = year
    
    # Výběr LVTV sloupce podle konfigurace
    lvtv_col = 'LVTV_O3' if USE_O3 else 'LVTV'
    
    if lvtv_col not in gdf.columns:
        print(f"  CHYBA: Sloupec {lvtv_col} nenalezen!")
        return None
    
    # Použití LVTV jako binární proměnné překročení (0/1)
    gdf['exceeded'] = gdf[lvtv_col].fillna(0).astype(int)
    
    n_exceeded = gdf['exceeded'].sum()
    pct_exceeded = n_exceeded / len(gdf) * 100
    
    print(f"  Překročení imisních limitů ({lvtv_col}):")
    print(f"    Vyhovující: {len(gdf) - n_exceeded} ({100-pct_exceeded:.1f}%)")
    print(f"    Překročeno: {n_exceeded} ({pct_exceeded:.1f}%)")
    
    return gdf


def load_all_years():
    """
    Načtení dat pro všechny roky
    """
    print("="*80)
    print("NAČÍTÁNÍ A PŘEDZPRACOVÁNÍ DAT (2021-2023)")
    print("="*80)
    
    yearly_data = {}
    
    for year, file_path in INPUT_FILES.items():
        gdf = load_and_preprocess_year(file_path, year)
        if gdf is not None:
            yearly_data[year] = gdf
    
    return yearly_data


# ============================================================================
# 2. ČASOVÁ SYNTÉZA (2020-2023)
# ============================================================================

def temporal_synthesis(yearly_data):
    """
    Časová syntéza - vyhodnocení počtu let s překročením pro každý grid
    """
    print("\n" + "="*80)
    print("ČASOVÁ SYNTÉZA - POČET LET S PŘEKROČENÍM")
    print("="*80)
    
    if not yearly_data:
        print("Žádná data k analýze!")
        return None
    lvtv_type = "S OZÓNEM (LVTV_O3)" if USE_O3 else "BEZ OZÓNU (LVTV)"
    print(f"Hodnocení: {lvtv_type}")
    print("="*80)
    
    if not yearly_data:
        print("Žádná data k analýze!")
        return None
    
    # Použití prvního roku jako základu
    base_year = min(yearly_data.keys())
    base_gdf = yearly_data[base_year].copy()
    
    # Počítání let s překročením pro každou gridovou buňku
    # Předpoklad: gridy mají stejný počet a pořadí ve všech letech
    years_exceeded = pd.Series(0, index=base_gdf.index)
    
    for year, gdf in yearly_data.items():
        if 'exceeded' in gdf.columns:
            years_exceeded += gdf['exceeded'].fillna(0)
    
    base_gdf['years_exceeded'] = years_exceeded
    
    # Kategorizace podle počtu let s překročením
    def categorize_exceedance(count):
        if count == 0:
            return 'stabilně vyhovující'
        elif count == 1:
            return 'epizodické překročení'
        elif count in [2, 3]:
            return 'opakované překročení'
        else:  # 4
            return 'dlouhodobé překročení'
    
    base_gdf['exceedance_category'] = years_exceeded.apply(categorize_exceedance)
    
    # Statistika
    print("\nRozdělení podle počtu let s překročením:")
    print(base_gdf['exceedance_category'].value_counts().sort_index())
    
    print("\nDetailní statistika:")
    for i in range(5):
        count = (years_exceeded == i).sum()
        pct = count / len(base_gdf) * 100
        print(f"  {i} let s překročením: {count:6d} gridů ({pct:5.1f}%)")
    
    # Index imisní zátěže = počet let s překročením (0-4)
    base_gdf['total_exceedance_index'] = years_exceeded
    
    print(f"\nCelkový index imisní zátěže (0-4):")
    print(f"  Průměr: {years_exceeded.mean():.2f}")
    print(f"  Medián: {years_exceeded.median():.0f}")
    print(f"  Maximum: {years_exceeded.max():.0f}")
    
    return base_gdf


# ============================================================================
# 3. PROSTOROVÁ TYPIZACE
# ============================================================================

def spatial_typology(gdf):
    """
    Prostorová typizace - rozdělení do typů A-E podle celkové zátěže
    """
    print("\n" + "="*80)
    print("PROSTOROVÁ TYPIZACE KVALITY OVZDUŠÍ")
    print("="*80)
    
    result_gdf = gdf.copy()
    
    # Kvantilové rozdělení do 5 typů
    percentiles = result_gdf['total_exceedance_index'].quantile([0.2, 0.4, 0.6, 0.8])
    
    def assign_type(value):
        if pd.isna(value):
            return 'Bez dat'
        elif value <= percentiles[0.2]:
            return 'A - velmi nízká zátěž'
        elif value <= percentiles[0.4]:
            return 'B - nízká zátěž'
        elif value <= percentiles[0.6]:
            return 'C - střední zátěž'
        elif value <= percentiles[0.8]:
            return 'D - vysoká zátěž'
        else:
            return 'E - velmi vysoká zátěž'
    
    result_gdf['air_quality_type'] = result_gdf['total_exceedance_index'].apply(assign_type)
    
    # Číselný kód typu pro další zpracování
    type_mapping = {
        'A - velmi nízká zátěž': 1,
        'B - nízká zátěž': 2,
        'C - střední zátěž': 3,
        'D - vysoká zátěž': 4,
        'E - velmi vysoká zátěž': 5,
        'Bez dat': 0
    }
    result_gdf['type_code'] = result_gdf['air_quality_type'].map(type_mapping)
    
    print("\nRozdělení do typů:")
    type_stats = result_gdf['air_quality_type'].value_counts().sort_index()
    print(type_stats)
    
    print("\nPrůměrný index zátěže podle typů:")
    type_summary = result_gdf.groupby('air_quality_type')['total_exceedance_index'].agg([
        'count', 'mean', 'min', 'max'
    ]).round(2)
    print(type_summary)
    
    return result_gdf


# ============================================================================
# 4. PROSTOROVÁ REGIONALIZACE (DISSOLVE)
# ============================================================================

def spatial_regionalization(gdf):
    """
    Prostorová regionalizace - sloučení sousedních gridů se stejným typem
    Vytvoří jedinečné regiony kvality ovzduší
    """
    print("\n" + "="*80)
    print("PROSTOROVÁ REGIONALIZACE - TVORBA REGIONŮ")
    print("="*80)
    
    # Dissolve podle typu kvality ovzduší
    # Zachováváme pouze typ a agregujeme geometrii
    dissolved = gdf[['air_quality_type', 'type_code', 'geometry']].dissolve(
        by='air_quality_type',
        aggfunc='first'
    ).reset_index()
    
    # Přidání statistik pro každý region
    # Spočítáme počet gridových buněk v každém regionu
    region_counts = gdf.groupby('air_quality_type').size().reset_index(name='grid_count')
    dissolved = dissolved.merge(region_counts, on='air_quality_type')
    
    # Výpočet plochy regionů
    dissolved['area_km2'] = dissolved.geometry.area / 1_000_000
    
    # Přidání průměrného indexu zátěže
    avg_index = gdf.groupby('air_quality_type')['total_exceedance_index'].mean().reset_index()
    dissolved = dissolved.merge(avg_index, on='air_quality_type')
    dissolved.rename(columns={'total_exceedance_index': 'avg_exceedance_index'}, inplace=True)
    
    # Přidání unikátního ID regionu
    dissolved['region_id'] = range(1, len(dissolved) + 1)
    
    print(f"\nVytvořeno {len(dissolved)} regionů kvality ovzduší")
    print("\nStatistiky regionů:")
    print(dissolved[['air_quality_type', 'grid_count', 'area_km2', 'avg_exceedance_index']].to_string(index=False))
    
    return dissolved


# ============================================================================
# 5. EXPORT VÝSLEDKŮ
# ============================================================================

def export_results(typology_gdf, regions_gdf, output_dir):
    """
    Export výsledků - typizace a regionalizace
    """
    print("\n" + "="*80)
    print("EXPORT VÝSLEDKŮ")
    print("="*80)
    
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # 1. Export typizace (všechny gridové buňky)
    typology_file = output_dir / 'air_quality_typology_2020_2023.gpkg'
    typology_gdf.to_file(typology_file, driver='GPKG')
    print(f"\nTypizace uložena: {typology_file}")
    print(f"  Počet gridových buněk: {len(typology_gdf)}")
    
    # 2. Export regionalizace (sloučené regiony)
    regions_file = output_dir / 'air_quality_regions_2020_2023.gpkg'
    regions_gdf.to_file(regions_file, driver='GPKG')
    print(f"\nRegionalizace uložena: {regions_file}")
    print(f"  Počet regionů: {len(regions_gdf)}")
    
    # 3. Export statistické sumarizace do CSV
    stats_file = output_dir / 'air_quality_statistics_2020_2023.csv'
    
    stats_summary = typology_gdf.groupby('air_quality_type').agg({
        'total_exceedance_index': ['count', 'mean', 'std', 'min', 'max']
    }).round(2)
    
    stats_summary.to_csv(stats_file)
    print(f"\nStatistiky uloženy: {stats_file}")
    
    # 4. Export detailního přehledu překročení
    exceedance_summary = typology_gdf[['air_quality_type', 'years_exceeded', 'exceedance_category']].groupby('air_quality_type').agg({
        'years_exceeded': ['count', 'mean', 'min', 'max']
    }).round(2)
    
    exceedance_file = output_dir / 'exceedance_by_type_2020_2023.csv'
    exceedance_summary.to_csv(exceedance_file)
    print(f"Přehled překročení uložen: {exceedance_file}")
    print(f"Přehled překročení uložen: {exceedance_file}")


# ============================================================================
# 6. HLAVNÍ PROGRAM
# ============================================================================

def main():
    """
    Hlavní funkce pro komplexní prostorovou syntézu kvality ovzduší
    """
    print("="*80)
    print("PROSTOROVÁ SYNTÉZA KVALITY OVZDUŠÍ ČR (2020–2023)")
    print("Hodnocení imisní zátěže na gridu 1×1 km (SRID 4258)")
    print("="*80)
    
    try:
        # 1. Načtení a předzpracování dat pro všechny roky
        yearly_data = load_all_years()
        
        if not yearly_data:
            print("\nERROR: Nepodařilo se načíst žádná data!")
            print("\nKONTROLA:")
            print(f"- Zkontrolujte cestu k datům: {DATA_DIR}")
            print(f"- Zkontrolujte, zda existují soubory:")
            for year, path in INPUT_FILES.items():
                print(f"  {year}: {path} - {'EXISTS' if path.exists() else 'MISSING'}")
            return
        
        # 2. Časová syntéza - vyhodnocení překročení přes roky
        temporal_result = temporal_synthesis(yearly_data)
        
        if temporal_result is None:
            return
        
        # 3. Prostorová typizace
        typology_result = spatial_typology(temporal_result)
        
        # 4. Prostorová regionalizace
        regions_result = spatial_regionalization(typology_result)
        
        # 5. Export výsledků
        export_results(typology_result, regions_result, OUTPUT_DIR)
        
        print("\n" + "="*80)
        print("ANALÝZA DOKONČENA!")
        print("="*80)
        print("\nVýstupy:")
        print("1. Syntetická mapa TYPIZACE - opakující se typy A-E")
        print("2. Syntetická mapa REGIONALIZACE - jedinečné regiony")
        print("3. Statistické přehledy v CSV")
        
    except Exception as e:
        print(f"\n{'='*80}")
        print("CHYBA PŘI ZPRACOVÁNÍ!")
        print("="*80)
        print(f"\nPopis chyby: {e}")
        
        import traceback
        print("\nDetailní traceback:")
        traceback.print_exc()
        
        print("\n" + "="*80)
        print("NÁPOVĚDA PRO OPRAVU:")
        print("="*80)
        print("1. Zkontrolujte názvy sloupců v atributových tabulkách")
        print("2. Upravte slovník POLLUTANTS podle skutečných názvů sloupců")
        print("3. Zkontrolujte, zda všechny tři soubory mají stejnou strukturu")
        print("4. Ověřte, že data jsou ve formátu GeoPackage (.gpkg)")


if __name__ == "__main__":
    main()
