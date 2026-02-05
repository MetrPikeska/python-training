import csv
from math import radians, sin, cos, sqrt, atan2

# Nová třída pro reprezentaci typu stanice
class TypStanice:
    def __init__(self, nazev_typu, popis):
        self.nazev_typu = nazev_typu
        self.popis = popis

    def vypis_info(self):
        print(f"Typ stanice: {self.nazev_typu} - {self.popis}")


# Upravená třída Stanice, která obsahuje odkaz na TypStanice
class Stanice:
    def __init__(self, nazev, lat, lon, typ_stanice):
        self.nazev = nazev
        self.lat = lat
        self.lon = lon
        self.typ_stanice = typ_stanice  # Odkaz na objekt TypStanice

    def vypis_info(self):
        print(f"Stanice: {self.nazev} na souřadnicích ({self.lat}, {self.lon})")
        self.typ_stanice.vypis_info()  # Volání metody vypis_info z TypStanice


if __name__ == "__main__":
    with open("stanice.csv", mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            # Odstranění mezer z názvů sloupců
            row = {key.strip(): value for key, value in row.items()}
            try:
                nazev = row['nazev']
                hodnoty = int(row['hodnoty'])
                lat = float(row['lat'])
                lon = float(row['lon'])
                typ = row['typ']

                # Vytvoření objektu TypStanice
                if typ == "meteo":
                    typ_stanice = TypStanice("meteo", "Meteorologická stanice")
                elif typ == "hydrologicka":
                    typ_stanice = TypStanice("hydrologicka", "Hydrologická stanice")
                else:
                    typ_stanice = TypStanice(typ, "Neznámý typ stanice")

                # Vytvoření objektu Stanice
                stanice = Stanice(nazev, lat, lon, typ_stanice)
                stanice.vypis_info()  # Výpis informací o stanici
            except KeyError as e:
                print(f"Chybí sloupec: {e} v řádku: {row}")
            except ValueError:
                print(f"Chyba při zpracování hodnot v řádku: {row}")






