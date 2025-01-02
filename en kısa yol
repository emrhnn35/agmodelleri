import networkx as nx


G = nx.DiGraph()
edges = [
    ("A", "B", 6),
    ("A", "D", 1),
    ("B", "C", 5),
    ("B", "E", 2),
    ("C", "F", 8),
    ("D", "B", 2),
    ("D", "E", 6),
    ("E", "F", 3)
]


G.add_weighted_edges_from(edges)
shortest_path = nx.single_source_dijkstra_path(G, source="A")
shortest_path_length = nx.single_source_dijkstra_path_length(G, source="A")
print("En Kısa Yollar:")
for target, path in shortest_path.items():
    print(f"A -> {target}: {path}")
print("\nEn Kısa Mesafeler:")
for target, distance in shortest_path_length.items():
    print(f"A -> {target}: {distance}")
