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


beskydy_vrcholy = [
    {"name": "Lysá hora", "elevation": 1323, "coordinates": [49.5900, 18.4461]},
    {"name": "Smrk", "elevation": 1276, "coordinates": [49.5244, 18.5247]},
    {"name": "Radhošť", "elevation": 1129, "coordinates": [49.5222, 18.4158]},
    {"name": "Kněhyně", "elevation": 1257, "coordinates": [49.4875, 18.4500]},
    {"name": "Velký Javorník", "elevation": 918, "coordinates": [49.3667, 18.4333]}]

for vrchol in beskydy_vrcholy:
    if vrchol["elevation"] > 1200:
        name = vrchol["name"]
        elevation = vrchol["elevation"]
        coordinates = vrchol["coordinates"]
        print(f"{name} - Elevation: {elevation} m, Coordinates: {coordinates}")
    else:
        print(f"{vrchol['name']} is below 1200 meters.")


