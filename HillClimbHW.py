h = {
    "A": 7,
    "B": 5,
    "C": 3,
    "U": 4,
    "E": 2,
    "G": 3,
    "I": 6,
    "J": 2,
    "K": 1,
    "Y": 2,
    "M": 0,
}

graph = {
    "A": ["B", "C", "U"],
    "B": ["E", "G"],
    "C": ["G", "I", "J"],
    "U": ["K", "Y"],
    "E": ["G", "M"],
    "G": ["M"],
    "I": ["M"],
    "J": ["K"],
    "K": ["J"],
    "Y": ["M"],
    "M": [],
}

current = "A"
path = ["A"]

print("Start at:", current)

while True:
    neighbors = graph[current]

    if len(neighbors) == 0:
        print("No more neighbors. Stopping.")
        break

    best_neighbor = neighbors[0]
    for neighbor in neighbors:
        if h[neighbor] < h[best_neighbor]:
            best_neighbor = neighbor

    if h[best_neighbor] >= h[current]:
        print("Stuck in a local minimum at:", current)
        break

    current = best_neighbor
    path.append(current)
    print("Moved to:", current)

print("Final Path:", path)