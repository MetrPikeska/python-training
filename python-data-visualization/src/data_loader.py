import csv

def load_data(filepath):
    data = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append({
                'nazev': row['nazev'],
                'nadmorska_vyska_m': int(row['nadmorska_vyska_m'])
            })
    return data