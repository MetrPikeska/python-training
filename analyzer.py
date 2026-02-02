import csv
import os

nejvyssi_vrchol = None
max_vyska = -1

data_csv = "C:\\Users\\Metr\\Documents\\GitHub\\python-training\\beskydy.csv"

with open(data_csv, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        nazev = row['nazev']
        nadmorska_vyska = int(row['nadmorska_vyska_m'])
        
        if nadmorska_vyska > max_vyska:
            max_vyska = nadmorska_vyska
            nejvyssi_vrchol = nazev


print(f"nejvyssi vrchol: {nejvyssi_vrchol}, vyska: {max_vyska} m")