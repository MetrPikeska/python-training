from math import radians, sin, cos, sqrt, atan2
import random as rnd
import time




# mesta = [39.904202, 116.407394]  # Beijing, China
# nyc = [40.712776, -74.005974]      # New York City, USA
# ldn = [51.507351, -0.127758]       # London, UK
# syd = [-33.868820, 151.209290]     # Sydney, Australia
# cpt = [-33.924870, 18.424055]      # Cape Town, South Africa

# def haversine(coord1, coord2):
#     from math import radians, sin, cos, sqrt, atan2

#     R = 6371.0  # Earth radius in kilometers

#     lat1, lon1 = coord1
#     lat2, lon2 = coord2

#     dlat = radians(lat2 - lat1)
#     dlon = radians(lon2 - lon1)

#     a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))

#     distance = R * c
#     return distance

# haversine_distance_nyc_ldn = haversine(syd, ldn)
# print(f"Distance between New York City and London: {haversine_distance_nyc_ldn:.2f} km")

# point = (39.904202, 116.407394)  # Beijing, China

# print(str(point[0]) +" " + str(point[1]))  # Latitude
# print(point[1])  # Longitude


# regions = [    "North America",
#     "South America", "Europe",
#     "Asia", "Africa", "Oceania"]

# region = set(regions)
# print("Unique regions:", regions)

# regions.append("Antarctica")
# print("Updated regions:", regions)

# regions.remove("South America")
# print("After removal:", regions)

# regions.sort()
# print("Sorted regions:", regions)

# print((len(regions)))  # Number of regions
# regions.remove("Europe")
# print("After removing Europe:", len(regions))

# city_attributes = {
#     "name" : "Praha",
#     "country" : "Czechia",
#     "population" : 1309000,
#     "coordinates" : [50.0755, 14.4378]
# }

# city_name = city_attributes["name"]
# city_population = city_attributes["population"]
# print(f"{city_name} has a population of {city_population} and is located at coordinates {city_attributes['coordinates']}.")

# city_attributes["mayor"] = "Zdeněk Hřib"
# print("Updated city attributes:", city_attributes)# # Geographical Coordinates of Various Cities

# print(city_attributes["coordinates"])


# beskydy_vrcholy = [
#     {"name": "Lysá hora", "elevation": 1323, "coordinates": [49.5900, 18.4461]},
#     {"name": "Smrk", "elevation": 1276, "coordinates": [49.5244, 18.5247]},
#     {"name": "Radhošť", "elevation": 1129, "coordinates": [49.5222, 18.4158]},
#     {"name": "Kněhyně", "elevation": 1257, "coordinates": [49.4875, 18.4500]},
#     {"name": "Velký Javorník", "elevation": 918, "coordinates": [49.3667, 18.4333]}]

# for vrchol in beskydy_vrcholy:
#     if vrchol["elevation"] > 1200:
#         name = vrchol["name"]
#         elevation = vrchol["elevation"]
#         coordinates = vrchol["coordinates"]
#         print(f"{name} - Elevation: {elevation} m, Coordinates: {coordinates}")
#     else:
#         print(f"{vrchol['name']} is below 1200 meters.")



# List of tuples representing coordinates



# counter = 0
# while counter < len(coordinates):
#     lat, lon = coordinates[counter]
#     print(f"Latitude: {lat}, Longitude: {lon}")
#     counter += 1


# for lat, lon in coordinates:
#     if lat > 0:
#         hemisphere = "Northern Hemisphere"
#     elif lat < 0:
#         hemisphere = "Southern Hemisphere"
#     else:
#         hemisphere = "Equator"
#     print(f"Latitude: {lat}, Longitude: {lon} is in the {hemisphere}.")

# for lat, lon in coordinates:
#     if lat > 0:
#         hemisphere = "Northern Hemisphere"
#     else:
#         hemisphere = "Southern Hemisphere"
    
#     if lon > 0:
#         direction = "Eastern Hemisphere"
#     else:
#         direction = "Western Hemisphere"
    
#     print(f"Latitude: {lat}, Longitude: {lon} is in the {hemisphere} and {direction}.")


# filtered_coords = []
# for lat, lon in coordinates:
#     if lat > 0 and lon > 0:
#         filtered_coords.append((lat, lon))
# print("Filtered Coordinates (Northern & Eastern Hemisphere):", filtered_coords)

# southern_count = 0

# for lat, lon in coordinates:
#     if lat < 0:
#         southern_count += 1
# print("Number of coordinates in the Southern Hemisphere:", southern_count)



# seznam_mest = [
#     {"name": "Tokyo", "coordinates": (35.6895, 139.6917)},
#     {"name": "Los Angeles", "coordinates": (34.0522, -118.2437)},
#     {"name": "London", "coordinates": (51.5074, -0.1278)},
#     {"name": "Sydney", "coordinates": (-33.8688, 151.2093)},
#     {"name": "Cape Town", "coordinates": (-33.9249, 18.4241)},
#     {"name": "Moscow", "coordinates": (55.7558, 37.6173)}
# ]

# for mesto in seznam_mest:
#     lat, lon = mesto["coordinates"]
#     if lat > 0:
#         hemisphere = "Northern Hemisphere"
#     else:
#         hemisphere = "Southern Hemisphere"
# print(f"{mesto['name']} is in the {hemisphere}.")

# counter = 0

# while counter < len(coordinates):
#     lat, lon  = seznam_mest[counter]
#     counter += 1
# #     print(seznam_mest)

# for lat, lon in coordinates:
#     if lon > 0:
#         direction = "Eastern Hemisphere"
#     else:
#         direction = "Western Hemisphere"
#     print(f"Latitude: {lat}, Longitude: {lon} is in the {direction}.")


# sum_southern = 0
# sum_northern = 0

# for lat, lon in coordinates:
#     if lon < 0:
#         sum_southern += 1
#     else:
#         sum_northern += 1

# print("Number of coordinates in the Western Hemisphere:", sum_southern, "Number of coordinates in the Eastern Hemisphere:", sum_northern)




# import random as rnd

# def generate_random_coordinates(n):
#     coordinates = []
#     for _ in range(n):
#         lat = rnd.uniform(-90, 90)
#         lon = rnd.uniform(-180, 180)
#         coordinates.append((lat, lon))
#     return coordinates

# for lat, lon in generate_random_coordinates(59):
#     if lat > 0 and lon > 0:
#         hemisphere = "Northern and Eastern Hemisphere"
#     elif lat > 0 and lon < 0:
#         hemisphere = "Northern and Western Hemisphere"
#     elif lat < 0 and lon > 0:
#         hemisphere = "Southern and Eastern Hemisphere"
#     else:
#         hemisphere = "Southern and Western Hemisphere"
#     print(f"Latitude: {lat}, Longitude: {lon} is in the {hemisphere}.")



# def multiply_coordinates(coord1, coord2):
#     lat1, lon1 = coord1
#     lat2, lon2 = coord2
#     return (lat1 * lat2, lon1 * lon2)
    


# print(multiply_coordinates((39.904202, 116.407394), (40.712776, -74.005974)))












