import networkx as nx # Mengimport library

G1 = nx.Graph() # Membuat graph kosong tidak berarah 

edges_europe = [ # Menambahkan edge pada graph yang telah dibuat 
    ("Arad", "Zerind", 75),
    ("Zerind", "Oradea", 71),
    ("Oradea", "Sibiu", 151),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75),
    ("Drobeta", "Craiova", 120),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Sibiu", "Rimnicu Vilcea", 80),
    ("Sibiu", "Fagaras", 99),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Pitesti", "Craiova", 138),
    ("Pitesti", "Bucharest", 101),
    ("Fagaras", "Bucharest", 211),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87)
]

G1.add_weighted_edges_from(edges_europe) # Menambahkan weight pada edge yg dibuat

shortest_paths_europe = dict(nx.all_pairs_dijkstra_path_length(G1)) # Menentukan jalur terpendek yang digunakan

for asal in shortest_paths_europe: # Membuat perulangan pada setia kota asal
    print(f"Dari {asal}:") # Menampilkan kota asal mana yang saat ini digunakan
    for tujuan, jarak in shortest_paths_europe[asal].items(): # Melakukan perulangan seluruh kota tujuan dan jarak terpendek dari kota asal
        print(f"  ke {tujuan} = {jarak}") # Menampilkan tujuan dan jarak
    print()
