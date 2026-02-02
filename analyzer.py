import csv
import os



data_csv = "C:\\Users\\Metr\\Documents\\GitHub\\python-training\\beskydy.csv"

def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

print(read_csv(data_csv))

