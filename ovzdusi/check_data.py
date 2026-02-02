"""
Diagnostický skript - kontrola hodnot v datech ČHMÚ
"""
import geopandas as gpd
import pandas as pd

# Načtení dat z roku 2020
file_path = r"C:\Skola\4_ZS\SYKAR\semestralka\V2\chmu_imise\chmu_imise_epsg4258_2020.gpkg"

print("Načítám data z roku 2020...")
gdf = gpd.read_file(file_path)

print(f"\nCelkem: {len(gdf)} gridových buněk")
print(f"\nSloupce: {list(gdf.columns)}")

# Kontrola hodnot pro každou látku
pollutants = {
    'SO2_day': 'SO2 4. nejvyšší 24h',
    'PM10_yr': 'PM10 roční průměr',
    'PM10_max36': 'PM10 36. nejvyšší 24h',
    'PM25_yr': 'PM2.5 roční průměr',
    'NO2_yr': 'NO2 roční průměr',
    'O3_max26': 'O3 26. max 8h',
    'AS_yr': 'As roční',
    'Cd_yr': 'Cd roční',
    'BaP_yr': 'Benzo[a]pyren',
    'BZN_yr': 'Benzen'
}

print("\n" + "="*80)
print("UKÁZKA HODNOT V DATECH")
print("="*80)

for col, name in pollutants.items():
    if col in gdf.columns:
        print(f"\n{name} ({col}):")
        print(f"  Typ dat: {gdf[col].dtype}")
        print(f"  Unikátní hodnoty (prvních 20): {gdf[col].unique()[:20]}")
        print(f"  Příklady hodnot:")
        print(gdf[[col]].head(10).to_string(index=False))
        
        # Zkus převést na čísla
        import re
        def parse_value(val):
            if pd.isna(val):
                return None
            val_str = str(val).strip()
            # Zjisti, jestli obsahuje <=, <, >=, >
            if '<=' in val_str or '>=' in val_str:
                return f"[OBSAHUJE OPERÁTOR: {val_str}]"
            val_clean = re.sub(r'[<>=\s]+', '', val_str)
            try:
                return float(val_clean)
            except:
                return f"[NELZE PŘEVÉST: {val_str}]"
        
        gdf[f'{col}_parsed'] = gdf[col].apply(parse_value)
        print(f"  Po parsování (prvních 10):")
        print(gdf[[col, f'{col}_parsed']].head(10).to_string(index=False))
        
        # Statistika parsovaných hodnot
        numeric_vals = [v for v in gdf[f'{col}_parsed'] if isinstance(v, (int, float))]
        if numeric_vals:
            print(f"  Min: {min(numeric_vals):.2f}, Max: {max(numeric_vals):.2f}, Průměr: {sum(numeric_vals)/len(numeric_vals):.2f}")
    else:
        print(f"\n{name} ({col}): SLOUPEC NEEXISTUJE!")

print("\n" + "="*80)
print("KONTROLA LVTV SLOUPCŮ")
print("="*80)
print("\nLVTV (překročení bez O3):")
print(gdf['LVTV'].value_counts())
print("\nLVTV_O3 (překročení s O3):")
print(gdf['LVTV_O3'].value_counts())
