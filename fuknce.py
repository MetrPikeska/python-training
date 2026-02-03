# def add (a, b):
#     return a + b

# result = add(2, 3)

# print("The sum is:", result)

# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# print(greet("Alice"))
# print(greet("Bob", "Hi"))

# print(greet(name="Charlie", greeting="Welcome"))


# def multyply(x, y):
#     return x * y
# def divide(x, y):
#     if y == 0:
#         return "Error: Division by zero"
#     return x / y

# result = multyply(4, 5)
# print("The product is:", result)



from math import radians, sin, cos, sqrt, atan2

# czech_cities = [
#     {"name": "Prague", "coords": (50.0755, 14.4378)},
#     {"name": "Ostrava", "coords": (49.8209, 18.2625)},
# ]

czech_cities = (
    {"name": "Prague", "coords": (50.0755, 14.4378)},
    {"name": "Ostrava", "coords": (49.8209, 18.2625)},
)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


# Example usage
distance = haversine(czech_cities[0]["coords"][0], czech_cities[0]["coords"][1],
                     czech_cities[1]["coords"][0], czech_cities[1]["coords"][1])
print(f"Distance: {distance:.2f} km")