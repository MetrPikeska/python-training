# Prostorová syntéza kvality ovzduší ČR (2020–2023)

Projekt pro vytvoření prostorové syntézy a regionalizace kvality ovzduší na území České republiky na základě imisních dat ČHMÚ.

## 📋 Popis projektu

Analýza imisní zátěže na gridu 1×1 km (SRID 4258) za období 2020–2023. Zahrnuje časovou syntézu překročení imisních limitů, prostorovou typizaci a regionalizaci.

## 🎯 Hlavní funkce

- **Časová syntéza** - vyhodnocení počtu let s překročením imisních limitů (0-4 roky)
- **Prostorová typizace** - rozdělení území do typů A-E podle imisní zátěže
- **Regionalizace** - sloučení sousedních gridových buněk do homogenních regionů
- **Export map** - výstup do formátu GeoPackage pro kartografii

## 📊 Hodnocené látky

Imisní limity pro ochranu lidského zdraví (zákon 201/2012 Sb.):
- SO₂ (4. nejvyšší 24hod. koncentrace)
- PM₁₀ (roční průměr, 36. nejvyšší 24hod. koncentrace)
- PM₂.₅ (roční průměr)
- NO₂ (roční průměr)
- O₃ (26. nejvyšší max. denní 8hod. klouzavý průměr za 3 roky)
- As, Cd (roční průměr)
- Benzo[a]pyren (roční průměr)
- Benzen (roční průměr)

## 🚀 Spuštění

```bash
# Aktivace virtuálního prostředí
.\venv\Scripts\Activate.ps1

# Spuštění analýzy
python air_synthesis.py
```

## 📁 Struktura projektu

```
python-training/
├── air_synthesis.py              # Hlavní skript analýzy
├── check_data.py                 # Diagnostický skript
├── spatial_synthesis_pollution.py # Pomocný skript
├── functions.py                  # Pomocné funkce
├── out/                          # Výstupní soubory (ignorováno v gitu)
│   ├── air_quality_typology_2020_2023.gpkg
│   ├── air_quality_regions_2020_2023.gpkg
│   ├── air_quality_statistics_2020_2023.csv
│   └── exceedance_by_type_2020_2023.csv
└── README.md
```

## 📈 Výstupy

1. **Typizace** (`air_quality_typology_2020_2023.gpkg`)
   - Gridová vrstva s typy A-E
   - Počet let s překročením pro každou buňku
   
2. **Regionalizace** (`air_quality_regions_2020_2023.gpkg`)
   - Sloučené regiony kvality ovzduší
   - Statistiky pro každý region
   
3. **Statistické přehledy** (CSV)
   - Souhrnné statistiky podle typů
   - Přehled překročení

## 🔧 Konfigurace

V souboru `air_synthesis.py` upravte:

```python
# Cesta k vstupním datům ČHMÚ
DATA_DIR = Path(r"C:\...\chmu_imise")

# Volba hodnocení (True = s ozónem, False = bez ozónu)
USE_O3 = True
```

## 📚 Použité knihovny

- `geopandas` - prostorová data
- `pandas` - analýza dat
- `numpy` - numerické výpočty

## 🎓 Účel

Projekt vytvořen pro předmět **Systematická kartografie (SYKAR)** na PřF UK.

## 📝 Metodika

Primárním zdrojem jsou stacionární měření ČHMÚ doplněná:
- Eulerovským chemickým disperzním modelem CAMx
- Gaussovským modelem SYMOS
- Evropským Eulerovským modelem EMEP
- Podpůrnými proměnnými (nadmořská výška, populační hustota)

## 📄 Licence

Vytvořeno pro akademické účely.

---

**Autor:** SYKAR projekt  
**Rok:** 2025-2026
