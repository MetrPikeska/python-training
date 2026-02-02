"""
Prostorová syntéza dat znečištění ovzduší z File Geodatabase
Vytvoření typů znečištění na základě průměrných koncentrací
"""

import geopandas as gpd
import pandas as pd
import numpy as np
from pathlib import Path

# Cesta k geodatabázi
gdb_path = r"C:\Skola\4_ZS\SYKAR\semestralka\fm\cz_ko_znecisteni_ovzdusi_4765596866114721526\5bbfb322-3183-4c52-88dd-88ae96ac250b.gdb"
layer_name = "cz_ko_znecisteni_ovzdusi"

def load_geodatabase_layer(gdb_path, layer_name):
    """Načtení vrstvy z File Geodatabase"""
    print(f"Načítám data z: {gdb_path}")
    print(f"Vrstva: {layer_name}")
    
    # Načtení dat pomocí geopandas
    gdf = gpd.read_file(gdb_path, layer=layer_name)
    #gdf = geodataframe 

    print(f"\nNačteno {len(gdf)} záznamů")
    print(f"Sloupce: {list(gdf.columns)}")
    print(f"\nPrvních 5 řádků:")
    print(gdf.head())
    
    return gdf



def analyze_pollution_data(gdf):
    """Analýza dat znečištění - zobrazení základních statistik"""
    print("\n" + "="*80)
    print("ANALÝZA DAT ZNEČIŠTĚNÍ")
    print("="*80)
    
    # Najít numerické sloupce (pravděpodobně koncentrace znečišťujících látek)
    numeric_cols = gdf.select_dtypes(include=[np.number]).columns.tolist()
    
    # Odstranit geometrické sloupce
    numeric_cols = [col for col in numeric_cols if col.lower() not in ['objectid', 'shape_length', 'shape_area', 'fid']]
    
    print(f"\nNumerické sloupce (pravděpodobně koncentrace): {numeric_cols}")
    
    if numeric_cols:
        print("\nZákladní statistiky:")
        print(gdf[numeric_cols].describe())
    
    return numeric_cols


def classify_pollution_types(gdf, concentration_columns, method='quantile', n_classes=5):
    """
    Klasifikace typů znečištění na základě koncentrací
    
    Parameters:
    -----------
    gdf : GeoDataFrame
        Data znečištění
    concentration_columns : list
        Seznam sloupců s koncentracemi
    method : str
        Metoda klasifikace: 'quantile', 'equal_interval', 'natural_breaks', 'custom'
    n_classes : int
        Počet tříd
    """
    print(f"\n{'='*80}")
    print(f"KLASIFIKACE TYPŮ ZNEČIŠTĚNÍ - Metoda: {method}")
    print(f"{'='*80}")
    
    result_gdf = gdf.copy()
    
    for col in concentration_columns:
        if col not in gdf.columns:
            continue
            
        data = gdf[col].dropna()
        
        if len(data) == 0:
            continue
        
        # Klasifikace podle zvolené metody
        if method == 'quantile':
            # Kvantilová klasifikace (stejný počet prvků v každé třídě)
            labels = [f'Třída {i+1}' for i in range(n_classes)]
            result_gdf[f'{col}_typ'] = pd.qcut(gdf[col], q=n_classes, labels=labels, duplicates='drop')
            
        elif method == 'equal_interval':
            # Klasifikace s rovnými intervaly
            labels = [f'Třída {i+1}' for i in range(n_classes)]
            result_gdf[f'{col}_typ'] = pd.cut(gdf[col], bins=n_classes, labels=labels)
            
        elif method == 'custom':
            # Vlastní klasifikace podle úrovní znečištění
            # Příklad: nízká, střední, vysoká, velmi vysoká
            percentiles = gdf[col].quantile([0.25, 0.50, 0.75, 0.90])
            
            def classify_custom(value):
                if pd.isna(value):
                    return 'Bez dat'
                elif value <= percentiles[0.25]:
                    return 'Nízké znečištění'
                elif value <= percentiles[0.50]:
                    return 'Střední znečištění'
                elif value <= percentiles[0.75]:
                    return 'Vysoké znečištění'
                elif value <= percentiles[0.90]:
                    return 'Velmi vysoké znečištění'
                else:
                    return 'Extrémní znečištění'
            
            result_gdf[f'{col}_typ'] = gdf[col].apply(classify_custom)
        
        # Výpis statistik klasifikace
        print(f"\nKlasifikace pro sloupec: {col}")
        print(result_gdf[f'{col}_typ'].value_counts().sort_index())
    
    return result_gdf


def create_combined_pollution_type(gdf, concentration_columns):
    """
    Vytvoření kombinovaného typu znečištění
    na základě průměru všech koncentrací
    """
    print(f"\n{'='*80}")
    print("VYTVOŘENÍ KOMBINOVANÉHO TYPU ZNEČIŠTĚNÍ")
    print(f"{'='*80}")
    
    result_gdf = gdf.copy()
    
    # Výpočet průměrné koncentrace ze všech látek
    valid_cols = [col for col in concentration_columns if col in gdf.columns]
    
    if valid_cols:
        result_gdf['prumerna_koncentrace'] = gdf[valid_cols].mean(axis=1)
        
        # Klasifikace kombinovaného typu
        percentiles = result_gdf['prumerna_koncentrace'].quantile([0.20, 0.40, 0.60, 0.80])
        
        def classify_combined(value):
            if pd.isna(value):
                return 'Bez dat'
            elif value <= percentiles[0.20]:
                return 'I - Velmi čistý vzduch'
            elif value <= percentiles[0.40]:
                return 'II - Čistý vzduch'
            elif value <= percentiles[0.60]:
                return 'III - Mírně znečištěný'
            elif value <= percentiles[0.80]:
                return 'IV - Znečištěný'
            else:
                return 'V - Silně znečištěný'
        
        result_gdf['typ_znecisteni'] = result_gdf['prumerna_koncentrace'].apply(classify_combined)
        
        print("\nRozdělení typů znečištění:")
        print(result_gdf['typ_znecisteni'].value_counts().sort_index())
        
        print("\nPrůměrné koncentrace pro jednotlivé typy:")
        summary = result_gdf.groupby('typ_znecisteni')['prumerna_koncentrace'].agg(['mean', 'min', 'max', 'count'])
        print(summary)
    
    return result_gdf


def spatial_synthesis(gdf, concentration_columns):
    """
    Prostorová syntéza - dissolve podle typu znečištění
    """
    print(f"\n{'='*80}")
    print("PROSTOROVÁ SYNTÉZA (DISSOLVE)")
    print(f"{'='*80}")
    
    if 'typ_znecisteni' not in gdf.columns:
        print("Nejprve je třeba vytvořit typy znečištění!")
        return None
    
    # Vybrat pouze numerické sloupce pro agregaci
    numeric_cols = gdf.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols = [col for col in numeric_cols if col.lower() not in ['objectid', 'fid']]
    
    # Dissolve podle typu znečištění s agregací pouze numerických sloupců
    dissolved = gdf[['typ_znecisteni', 'geometry'] + numeric_cols].dissolve(
        by='typ_znecisteni', 
        aggfunc='mean'
    )
    dissolved = dissolved.reset_index()
    
    print(f"\nVýsledek syntézy: {len(dissolved)} polygonů")
    print("\nTypy znečištění a jejich plochy:")
    
    # Výpočet ploch
    dissolved['plocha_km2'] = dissolved.geometry.area / 1_000_000  # převod na km²
    
    summary = dissolved[['typ_znecisteni', 'plocha_km2']].sort_values('typ_znecisteni')
    print(summary.to_string(index=False))
    
    return dissolved


def export_results(gdf, output_path, format='shapefile'):
    """
    Export výsledků do souboru
    
    Parameters:
    -----------
    gdf : GeoDataFrame
        Data k exportu
    output_path : str
        Cesta pro uložení
    format : str
        'shapefile', 'geojson', 'gpkg'
    """
    print(f"\n{'='*80}")
    print(f"EXPORT VÝSLEDKŮ")
    print(f"{'='*80}")
    
    output_path = Path(output_path)
    
    if format == 'shapefile':
        output_file = output_path / 'typy_znecisteni.shp'
        gdf.to_file(output_file)
    elif format == 'geojson':
        output_file = output_path / 'typy_znecisteni.geojson'
        gdf.to_file(output_file, driver='GeoJSON')
    elif format == 'gpkg':
        output_file = output_path / 'typy_znecisteni.gpkg'
        gdf.to_file(output_file, driver='GPKG')
    
    print(f"Data exportována do: {output_file}")
    print(f"Počet záznamů: {len(gdf)}")


def main():
    """Hlavní funkce pro prostorovou syntézu dat znečištění"""
    
    try:
        # 1. Načtení dat z geodatabáze
        gdf = load_geodatabase_layer(gdb_path, layer_name)
        
        # 2. Analýza dat a nalezení sloupců s koncentracemi
        concentration_cols = analyze_pollution_data(gdf)
        
        if not concentration_cols:
            print("\nNENALEZENY SLOUPCE S KONCENTRACEMI!")
            print("Prosím, zadejte názvy sloupců ručně:")
            print(f"Dostupné sloupce: {list(gdf.columns)}")
            return
        
        # 3. Klasifikace typů znečištění pro jednotlivé látky
        # Můžete zvolit metodu: 'quantile', 'equal_interval', 'custom'
        gdf_classified = classify_pollution_types(gdf, concentration_cols, method='custom')
        
        # 4. Vytvoření kombinovaného typu znečištění
        gdf_with_types = create_combined_pollution_type(gdf_classified, concentration_cols)
        
        # 5. Prostorová syntéza (dissolve podle typů)
        gdf_dissolved = spatial_synthesis(gdf_with_types, concentration_cols)
        
        # 6. Export výsledků
        # Můžete změnit cestu a formát
        output_dir = Path.cwd()
        
        # Export detailních dat (všechny polygony s typy)
        export_results(gdf_with_types, output_dir, format='gpkg')
        
        # Export syntetizovaných dat (dissolve)
        if gdf_dissolved is not None:
            gdf_dissolved_copy = gdf_dissolved.copy()
            gdf_dissolved_copy.to_file(output_dir / 'typy_znecisteni_synteza.gpkg', driver='GPKG')
            print(f"Syntetizovaná data uložena: {output_dir / 'typy_znecisteni_synteza.gpkg'}")
        
        print("\n" + "="*80)
        print("HOTOVO!")
        print("="*80)
        
    except Exception as e:
        print(f"\nChyba při zpracování: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
