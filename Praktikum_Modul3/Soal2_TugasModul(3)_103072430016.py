import networkx as nx # Mengimport library

G1 = nx.Graph() # Membuat graph kosong tidak berarah 

edges_indo = [ # Membuat edge pada graph yg telah dibuat
    ("Jakarta", "Cirebon", 327),
    ("Jakarta", "Bandung", 270),
    ("Bandung", "Cirebon", 120),
    ("Bandung", "Yogyakarta", 373),
    ("Cirebon", "Semarang", 305),
    ("Cirebon", "Yogyakarta", 210),
    ("Yogyakarta", "Semarang", 109),
    ("Semarang", "Surakarta", 97),
    ("Yogyakarta", "Surakarta", 60),
    ("Semarang", "Surabaya", 369),
    ("Surakarta", "Malang", 370),
    ("Surabaya", "Malang", 94)
]

G1.add_weighted_edges_from(edges_indo) # Menambahkan weight pada graph

shortest_paths_indo = dict(nx.all_pairs_dijkstra_path_length(G1)) # Menentukan jalur terpendek yang akan digunakan

for asal in shortest_paths_indo: # Melakukan perulangan untuk setiap kota asal
    print(f"Dari {asal}:") # Menampilkan kota asal saat ini 
    for tujuan, jarak in shortest_paths_indo[asal].items(): # Melakukan perulangan tujuan + jarak terpendek yang digunakan
        print(f"  ke {tujuan} = {jarak}") # Menampilkan tujuan dan jaraknya
    print()
