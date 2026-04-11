import networkx as nx # Melakukan import dari library
import matplotlib.pyplot as plt # Melakukan import dari library

# Fungsi show_graph dari modul sebelumnya
def show_graph(G, pos=None, title="Graf"):
    plt.figure(figsize=(8, 5))
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=1500, font_size=12, font_weight='bold', arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.axis('off')
    plt.show()

G = nx.Graph() # Membuat graph untuk tree

edges = [ # Menambahkan edge sesuai dengan struktur tree 
    ('A', 'B'), 
    ('A', 'C'),
    ('B', 'D'), 
    ('B', 'E'),
    ('C', 'F'), 
    ('C', 'G')
]
G.add_edges_from(edges)

# Menentukan posisi dari edge agar berbentuk seperti tree
pos = {
    'A': (0, 3),
    'B': (-2, 2), 
    'C': (2, 2),
    'D': (-3, 1), 
    'E': (-1, 1),
    'F': (1, 1),  
    'G': (3, 1)
}

show_graph(G, pos, title="Graf Tree") # Menampilkan graph yang sudah dibuat 

bfs_edges = list(nx.bfs_edges(G, source='A')) # Menampilkan BFS dari Node A 

print("Urutan BFS (edge):") # Menampilkan urutan BFS dalam bentuk edge 
for edge in bfs_edges:
    print(f"  {edge[0]} -> {edge[1]}")

bfs_nodes = ['A'] + [v for u, v in bfs_edges] # Menampilkan urutan BFS dalam bentuk node 
print("\nUrutan BFS (node):")
print(" ->".join(bfs_nodes))
