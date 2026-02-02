points = [
    [35.6895, 139.6917],  # Tokyo
    [34.0522, -118.2437],  # Los Angeles
    [51.5074, -0.1278],  # London
    [48.8566, 2.3522],  # Paris
]

centroid_lat = sum(point[0] for point in points) / len(points)
centroid_lon = sum(point[1] for point in points) / len(points)
centroid = [centroid_lat, centroid_lon]
print("Centroid:", centroid)