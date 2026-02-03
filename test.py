import math

stanice_data = [
    {"nazev": "Ostrava", "souradnice": (49.8209, 18.2625), "teplota": [19]},
    {"nazev": "Brno", "souradnice": (49.1951, 16.6068), "teplota": [15]},
    {"nazev": "Praha", "souradnice": (50.0755, 14.4378), "teplota": [13]},
    {"nazev": "Plzen", "souradnice": (49.7475, 13.3776), "teplota": [10]},
    {"nazev": "Liberec", "souradnice": (50.7671, 15.0562), "teplota": [8]},
    {"nazev": "Olomouc", "souradnice": (49.5938, 17.2509), "teplota": [12]},
    {"nazev": "Hradec Kralove", "souradnice": (50.2092, 15.8328), "teplota": [9]}
]

def vypocitej_prumer(hodnoty):
    """Vypočítá průměr ze seznamu hodnot. Vrací 0 pro prázdný seznam."""
    if not hodnoty:
        return 0
    return sum(hodnoty) / len(hodnoty)

# Hlavní zpracování
vsechny_prumery = []
nadprumerne_stanice = []
podprumerne_stanice = []

# Prahová hodnota pro "nadprůměr" (v původním kódu bylo 15000, což nedává smysl pro teploty kolem 15)
# Předpokládám, že šlo o překlep a mělo tam být např. 12
PRAH_TEPLOTY = 12

for stanice in stanice_data:
    prumer = vypocitej_prumer(stanice["teplota"])
    vsechny_prumery.append(prumer)
    
    print(f"Stanice {stanice['nazev']} má průměrnou teplotu: {prumer:.1f}°C")
    
    if prumer > PRAH_TEPLOTY:
        nadprumerne_stanice.append(stanice["nazev"])
    else:
        podprumerne_stanice.append(stanice["nazev"])

print("\n--- Souhrn ---")
print(f"Všechny průměrné teploty: {vsechny_prumery}")
print(f"Stanice s nadprůměrnou teplotou (>{PRAH_TEPLOTY}): {nadprumerne_stanice}")
print(f"Stanice s podprůměrnou teplotou (<={PRAH_TEPLOTY}): {podprumerne_stanice}")

# Výpočty souřadnic (původně zakomentované, nyní vyčištěné)
northest_point = max(stanice_data, key=lambda x: x["souradnice"][0])
print(f"\nNejsevernější stanice je {northest_point['nazev']} na souřadnicích {northest_point['souradnice']}")

brno_coords = (49.1951, 16.6068)
euklidovska_vzdalenost = math.sqrt(
    (northest_point["souradnice"][0] - brno_coords[0]) ** 2 + 
    (northest_point["souradnice"][1] - brno_coords[1]) ** 2
)
print(f"Euklidovská vzdálenost mezi {northest_point['nazev']} a Brnem je {euklidovska_vzdalenost:.2f} stupňů.")
