import csv
import os
import sys
import math



# beskdy_vrcholy = "C:\\Users\\Metr\\Documents\\GitHub\\python-training\\beskydy.csv"



# with open(beskdy_vrcholy, mode='r', encoding='utf-8') as file:
#     csv_reader = csv.DictReader(file)

#     print("Seznam vrcholů v Beskydech:")
#     for row in csv_reader:
#         nazev = row['nazev']
#         nadmorska_vyska = row['nadmorska_vyska_m']
        
        
#         nazev_upper = nazev.upper()

#         print(f"Vrchol: {nazev_upper}, Nadmorská výška: {nadmorska_vyska} m")


# # # Seznam pro uložení všech nadmořských výšek
# # nadmorske_vysky = []
# # with open(beskdy_vrcholy, mode='r', encoding='utf-8') as file:
# #     csv_reader = csv.DictReader(file)

# #     for row in csv_reader:
# #         nazev = row['nazev']
# #         nadmorska_vyska = int(row['nadmorska_vyska_m'])
# #         nadmorske_vysky.append(nadmorska_vyska)
# #         print(f"Vrchol: {nazev}, Nadmorská výška: {nadmorska_vyska} m")

# # # Výpočet min/max ze seznamu
# # min_height = min(nadmorske_vysky)
# # max_height = max(nadmorske_vysky)

# # print(f"\nMinimální výška: {min_height} m")
# # print(f"Maximální výška: {max_height} m")





# beskdy_vrcholy = "C:\\Users\\Metr\\Documents\\GitHub\\python-training\\beskydy.csv"

# with open(beskdy_vrcholy, mode='r', encoding='utf-8') as file:
#     csv_reader = csv.DictReader(file)

#     for row in csv_reader:
#         nazev = row['nazev']
#         nadmorska_vyska = int(row['nadmorska_vyska_m'])
        
#         # Parsování souřadnic
#         coord_str = row['zemepisne_souradnice']
#         lat_str, lon_str = coord_str.split(',')
#         lat_str = lat_str.strip()
#         lon_str = lon_str.strip()
        
#         latitude = float(lat_str[:-1]) * (1 if lat_str[-1] == 'N' else -1)
#         longitude = float(lon_str[:-1]) * (1 if lon_str[-1] == 'E' else -1)
        
#         print(f"{nazev}: {nadmorska_vyska}m, GPS: {latitude}, {longitude}")





# city_lowercase = {city["name"].lower(): city for city in city_coordinates}
# print(city_lowercase)

# lat_str, lon_str = city_lowercase["praha"]["coordinates"]

# lat = float(lat_str[:-1]) * (1 if lat_str[-1] == 'N' else -1)
# lon = float(lon_str[:-1]) * (1 if lon_str[-1] == 'E' else -1)

# print(f"Latitude: {lat}, Longitude: {lon}")

def format(city_coordinates):
    formatted_list = []
    for city in city_coordinates:
        name = city["name"]
        lat_str, lon_str = city["coordinates"]
        latitude = float(lat_str[:-1]) * (1 if lat_str[-1] == 'N' else -1)
        longitude = float(lon_str[:-1]) * (1 if lon_str[-1] == 'E' else -1)
        formatted_list.append({
            "name": name,
            "latitude": latitude,
            "longitude": longitude
        })
    return formatted_list

city_coordinates = [
    {"name": "Praha", "coordinates": ["50.0755N", "14.4378E"]},
    {"name": "Ostrava", "coordinates": ["49.8209N", "18.2625E"]},
    {"name": "Brno", "coordinates": ["49.1951N", "16.6068E"]},
    {"name": "Olomouc", "coordinates": ["49.5938N", "17.2509E"]}
]

formatted_coordinates = format(city_coordinates)
for city in formatted_coordinates:
    print(f"{city['name']}: Latitude = {city['latitude']}, Longitude = {city['longitude']}")
    # 


















