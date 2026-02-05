import csv
from math import radians, sin, cos, sqrt, atan2

class Stanice:
    def __init__(self, nazev, lat, lon):
        self.nazev = nazev
        self.lat = lat
        self.lon = lon

    def vypis_info(self):
        print(f"Stanice: {self.nazev} na souřadnicích ({self.lat}, {self.lon})")

# Tento kód se spustí pouze tehdy, když je soubor spuštěn přímo
if __name__ == "__main__":
    praha = Stanice("Praha", 50.07, 14.43)
    brno = Stanice("Brno", 49.19, 16.60)

    praha.vypis_info()
    brno.vypis_info()

