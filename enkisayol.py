import networkx as nx

G = nx.DiGraph()
kenarlar = [
    ("A", "B", 6),
    ("A", "D", 1),
    ("B", "C", 5),
    ("B", "E", 2),
    ("C", "F", 8),
    ("D", "B", 2),
    ("D", "E", 6),
    ("E", "F", 3)
]

G.add_weighted_edges_from(kenarlar)
en_kisa_yol = nx.single_source_dijkstra_path(G, source="A")
en_kisa_yol_uzunlugu = nx.single_source_dijkstra_path_length(G, source="A")
print("En Kısa Yollar:")
for hedef, yol in en_kisa_yol.items():
    print(f"A -> {hedef}: {yol}")
print("\nEn Kısa Mesafeler:")
for hedef, mesafe in en_kisa_yol_uzunlugu.items():
    print(f"A -> {hedef}: {mesafe}")
