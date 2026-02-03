# Zadání: Geofencing – Jsou stanice v zájmové oblasti?
# Jako geoinformatik často řešíš, jestli se nějaký bod nachází uvnitř určitého území. My si to zjednodušíme na tzv. Bounding Box (obdélníkovou oblast).

# Tvůj úkol:
# Máš stejný seznam stanic jako minule (můžeš ho zkopírovat). Tvým úkolem je:

# Definuj hranice oblasti: Vytvoř si čtyři proměnné (nebo jeden slovník), které budou představovat "hranice" zájmového území:

# min_lat, max_lat (zeměpisná šířka)

# min_lon, max_lon (zeměpisná délka)

# (Např. oblast kolem Prahy: lat 49.9 až 50.2, lon 14.2 až 14.6).

# Obohať data: Projdi seznam stanic cyklem a do každého slovníku (ke každé stanici) přidej nový klíč "v_oblasti".

# Hodnota bude True, pokud souřadnice stanice leží uvnitř tvých hranic.

# Hodnota bude False, pokud leží mimo.

# Vypiš výsledek: Na konci vypiš seznam všech stanic ve formátu:

# "Stanice [název] leží v oblasti: [ANO/NE]"

# Bonus: Spočítej, kolik stanic celkem se v oblasti nachází (použij k tomu proměnnou, kterou v cyklu budeš zvyšovat o 1).


stanice_data = [
    {"nazev": "Ostrava", "souradnice": (49.8209, 18.2625), "teplota": [19]},
    {"nazev": "Brno", "souradnice": (49.1951, 16.6068), "teplota": [15]},
    {"nazev": "Praha", "souradnice": (50.0755, 14.4378), "teplota": [13]},
    {"nazev": "Plzen", "souradnice": (49.7475, 13.3776), "teplota": [10]},
    {"nazev": "Liberec", "souradnice": (50.7671, 15.0562), "teplota": [8]},
    {"nazev": "Olomouc", "souradnice": (49.5938, 17.2509), "teplota": [12]},
    {"nazev": "Hradec Kralove", "souradnice": (50.2092, 15.8328), "teplota": [9]}
]


geo_fance_box = {
    "min_lat": 49.9,
    "max_lat": 50.2,
    "min_lon": 14.2,
    "max_lon": 14.6
}


for stanice in stanice_data:
    lat, lon = stanice["souradnice"]
    if (geo_fance_box["min_lat"] <= lat <= geo_fance_box["max_lat"] and
        geo_fance_box["min_lon"] <= lon <= geo_fance_box["max_lon"]):
        stanice["v_oblasti"] = True
    else:
        stanice["v_oblasti"] = False
        status = "ANO" if stanice["v_oblasti"] else "NE"
    print(f"Stanice {stanice['nazev']} leží v oblasti: {status}")

# Bonus: Spočítej, kolik stanic celkem se v oblasti nachází (použij k tomu proměnnou, kterou v cyklu budeš zvyšovat o 1).
pocet_v_oblasti = sum(1 for stanice in stanice_data if stanice["v_oblasti"])
print(f"\nCelkem stanic v oblasti: {pocet_v_oblasti}")

for stanice in stanice_data:
    print("Stanice:", stanice)