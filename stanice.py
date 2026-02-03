import stanice
from math import radians, sin, cos, sqrt, atan2
import csv

data_file = 'stanice.csv'

import csv

data_ze_souboru = []
with open('stanice.csv', mode='r', encoding='utf-8') as soubor:
    reader = csv.DictReader(soubor)
    for radek in reader:
        # Pozor: CSV načítá všechno jako text, souřadnice musíš převést na float!
        radek['lat'] = float(radek['lat'])
        radek['lon'] = float(radek['lon'])
        data_ze_souboru.append(radek)

print(data_ze_souboru[0]) # Vypíše první stanici jako slovník

