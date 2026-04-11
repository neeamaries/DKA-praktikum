import networkx as nx # Melakukan impor dari library 
import matplotlib.pyplot as plt # Melakukan impor dari library 

def show_graph(G, pos=None, title="Graf"): # Fungsi pada show graph
    plt.figure(figsize=(8, 5))
    if pos is None:
        pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=2500, font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.axis('off')
    plt.show()

G2 = nx.Graph() # Digunakan untuk membuat graph berbobot 

G2.add_weighted_edges_from([ # Menambahkan bobot pada edge yang telah dibuat 
    ('Bandung', 'Jakarta', 150),
    ('Bandung', 'Yogyakarta', 380),
    ('Jakarta', 'Semarang', 450),
    ('Yogyakarta', 'Surabaya', 330),
    ('Semarang', 'Surabaya', 350)
])

pos2 = { # Menentukan posisi node pada bobot yang dibuat 
    'Bandung':(0, 1),
    'Jakarta':(-2, 2),
    'Yogyakarta':(2, 2),
    'Semarang':(-1, 3),
    'Surabaya':(3, 3)
}

show_graph(G2, pos2, title="Graf Berbobot Antar Kota") # Menampilkan hasil graph yang sudah dibuat 

# Menampilkan BFS yang dimulai dari kota Bandung 
bfs_edges2 = list(nx.bfs_edges(G2, source='Bandung'))

# Menampilkan urutan BFS melalui edge 
print("Urutan BFS dari Bandung (edge):")
for edge in bfs_edges2:
    print(f"  {edge[0]} -> {edge[1]}")

bfs_nodes2 = ['Bandung'] + [v for u, v in bfs_edges2]
print("\nUrutan BFS (node):")
print(" -> ".join(bfs_nodes2))
