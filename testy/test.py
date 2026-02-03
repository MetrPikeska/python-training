# import math

# stanice_data = [
#     {"nazev": "Ostrava", "souradnice": (49.8209, 18.2625), "teplota": [19]},
#     {"nazev": "Brno", "souradnice": (49.1951, 16.6068), "teplota": [15]},
#     {"nazev": "Praha", "souradnice": (50.0755, 14.4378), "teplota": [13]},
#     {"nazev": "Plzen", "souradnice": (49.7475, 13.3776), "teplota": [10]},
#     {"nazev": "Liberec", "souradnice": (50.7671, 15.0562), "teplota": [8]},
#     {"nazev": "Olomouc", "souradnice": (49.5938, 17.2509), "teplota": [12]},
#     {"nazev": "Hradec Kralove", "souradnice": (50.2092, 15.8328), "teplota": [9]}
# ]

# def vypocitej_prumer(hodnoty):
#     """Vypočítá průměr ze seznamu hodnot. Vrací 0 pro prázdný seznam."""
#     if not hodnoty:
#         return 0
#     return sum(hodnoty) / len(hodnoty)

# # Hlavní zpracování
# vsechny_prumery = []
# nadprumerne_stanice = []
# podprumerne_stanice = []

# # Prahová hodnota pro "nadprůměr" (v původním kódu bylo 15000, což nedává smysl pro teploty kolem 15)
# # Předpokládám, že šlo o překlep a mělo tam být např. 12
# PRAH_TEPLOTY = 12

# for stanice in stanice_data:
#     prumer = vypocitej_prumer(stanice["teplota"])
#     vsechny_prumery.append(prumer)
    
#     print(f"Stanice {stanice['nazev']} má průměrnou teplotu: {prumer:.1f}°C")
    
#     if prumer > PRAH_TEPLOTY:
#         nadprumerne_stanice.append(stanice["nazev"])
#     else:
#         podprumerne_stanice.append(stanice["nazev"])

# print("\n--- Souhrn ---")
# print(f"Všechny průměrné teploty: {vsechny_prumery}")
# print(f"Stanice s nadprůměrnou teplotou (>{PRAH_TEPLOTY}): {nadprumerne_stanice}")
# print(f"Stanice s podprůměrnou teplotou (<={PRAH_TEPLOTY}): {podprumerne_stanice}")

# # Výpočty souřadnic (původně zakomentované, nyní vyčištěné)
# northest_point = max(stanice_data, key=lambda x: x["souradnice"][0])
# print(f"\nNejsevernější stanice je {northest_point['nazev']} na souřadnicích {northest_point['souradnice']}")

# brno_coords = (49.1951, 16.6068)
# euklidovska_vzdalenost = math.sqrt(
#     (northest_point["souradnice"][0] - brno_coords[0]) ** 2 + 
#     (northest_point["souradnice"][1] - brno_coords[1]) ** 2
# )
# print(f"Euklidovská vzdálenost mezi {northest_point['nazev']} a Brnem je {euklidovska_vzdalenost:.2f} stupňů.")



import math

stanice_data = [
    {"nazev": "Ostrava", "souradnice": (49.8209, 18.2625), "hodnoty": [20000]},
    {"nazev": "Brno", "souradnice": (49.1951, 16.6068), "hodnoty": [15000]},
    {"nazev": "Praha", "souradnice": (50.0755, 14.4378), "hodnoty": [30000]},
    {"nazev": "Plzen", "souradnice": (49.7475, 13.3776), "hodnoty": [10000]},
    {"nazev": "Liberec", "souradnice": (50.7671, 15.0562), "hodnoty": [8000]},
    {"nazev": "Olomouc", "souradnice": (49.5938, 17.2509), "hodnoty": [12000]},
    {"nazev": "Hradec Kralove", "souradnice": (50.2092, 15.8328), "hodnoty": [9000]}
]

# 1. Výpočet průměru všech hodnot napříč stanicemi
vsechny_hodnoty = [sum(s["hodnoty"]) / len(s["hodnoty"]) for s in stanice_data]
celkovy_prumer = sum(vsechny_hodnoty) / len(vsechny_hodnoty)
print(f"Celkový průměr všech stanic: {celkovy_prumer:.2f}\n")

# 2. Filtrace stanic nad průměrem
print("Stanice s nadprůměrnou hodnotou:")
nadprumerne = [s["nazev"] for s in stanice_data if (sum(s["hodnoty"])/len(s["hodnoty"])) > celkovy_prumer]
print(", ".join(nadprumerne))

# 3. Nejsevernější bod
nejsevernejsi = max(stanice_data, key=lambda x: x["souradnice"][0])
print(f"\nNejsevernější stanice: {nejsevernejsi['nazev']} ({nejsevernejsi['souradnice'][0]}°N)")

# 4. Bonus: Funkce pro vzdálenost
def vypocitej_vzdalenost(bod_a, bod_b):
    lat1, lon1 = bod_a["souradnice"]
    lat2, lon2 = bod_b["souradnice"]
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

# Příklad pro Liberec a Brno
brno = stanice_data[1]
vzdalenost = vypocitej_vzdalenost(nejsevernejsi, brno)
print(f"Vzdálenost {nejsevernejsi['nazev']} -> {brno['nazev']}: {vzdalenost:.2f} stupňů.")