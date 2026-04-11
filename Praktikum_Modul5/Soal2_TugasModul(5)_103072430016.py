import networkx as nx # Melakukan import dari library
import matplotlib.pyplot as plt # Melakukan import dari library


def show_graph(G, pos=None, title=''): 
    plt.figure(figsize=(14, 10))
    if pos is None:
        pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='white',
        node_size=2000,
        node_shape='s',
        edgecolors='black',
        font_color="black",
        font_weight="bold",
        font_size=10,
        width=2
    )
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_color='black',
        font_weight="bold",
        font_size=12,
    )
    plt.margins(0.2)
    plt.title(title)
    plt.show()


# Menentukan posisi dari tiap kota pada graph
pos_jawa = {
    'Jakarta':(1,10),
    'Bandung':(3, 3),
    'Cirebon':(5, 8),
    'Yogyakarta': (8,1),
    'Semarang':(8.7, 7.5),
    'Surakarta':(11, 4),
    'Malang':(15, 1.5),
    'Surabaya':(18, 8),
}

G_jawa = nx.Graph() # Membuat graph kosongan

edges_jawa = [
    ('Jakarta','Cirebon', 327),
    ('Jakarta','Bandung', 270),
    ('Cirebon','Bandung', 120),
    ('Cirebon','Semarang',305),
    ('Bandung', 'Yogyakarta', 373),
    ('Semarang','Yogyakarta', 109),
    ('Semarang','Surabaya', 369),
    ('Semarang','Surakarta',97),
    ('Yogyakarta','Surakarta',60),
    ('Surakarta','Surabaya',370),
    ('Surabaya','Malang',94),
]

for u, v, w in edges_jawa:
    G_jawa.add_edge(u, v, weight=w)

# Menampilkan graph yang sudah dibuat 
show_graph(G_jawa, pos=pos_jawa, title='Graf Pulau Jawa (Weighted)')

# Menampilkan BFS yang dimulai dari Bandung 
print("\nUrutan node yang dikunjungi (BFS dari Bandung):")
for i, (u, v) in enumerate(nx.bfs_edges(G_jawa, source='Bandung'), start=1):
    print(f"{i}. {u} -> {v}")
