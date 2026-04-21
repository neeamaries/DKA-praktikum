import networkx as nx
import matplotlib.pyplot as plt

def show_graph(G, pos=None, title=''):
    plt.figure(figsize=(14,10))
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

pos_eropa = {
    'Arad':(0, 9),
    'Zerind': (6, 15),
    'Oradea': (9, 21),
    'Timisoara': (3, 3),
    'Lugoj': (9, 3),
    'Mehadia':(12, -1.5),
    'Drobeta':(9, -6),
    'Sibiu':  (18, 12),
    'Fagaras':(27, 12),
    'Rimnicu Vilcea': (18, 6),
    'Pitesti':(24, 6),
    'Craiova':(18, -3),
    'Bucharest':(36, 3),
    'Giurgiu':(36, -3),
    'Urziceni':(42, 3),
    'Hirsova':(48, 3),
    'Eforie': (51, -3),
    'Vaslui': (48, 12),
    'Iasi':   (48, 18),
    'Neamt':  (42, 21),
}

G_eropa = nx.Graph()

edges_eropa = [
    ("Arad", "Zerind", 75),
    ("Arad", "Timisoara", 118),
    ("Arad", "Sibiu", 140),
    ("Zerind", "Oradea", 71),
    ("Oradea", "Sibiu", 151),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75),
    ("Drobeta", "Craiova", 120),
    ("Craiova", "Pitesti", 138),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Sibiu", "Fagaras", 99),
    ("Sibiu", "Rimnicu Vilcea", 80),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87),
]

for u, v, w in edges_eropa:
    G_eropa.add_edge(u, v, weight=w)

print("Elemen pada Graf Eropa:")
print("Node:", G_eropa.nodes())
print("Edge:", G_eropa.edges())

show_graph(G_eropa, pos=pos_eropa, title='Graf Kota Eropa')

print("\nDFS Graf Eropa:")
i = 1
for u, v in nx.dfs_edges(G_eropa, source='Arad'):
    print(f"{i}. {u} - {v}")
    i += 1

pos_jawa = {
    'Jakarta':    (1, 10),
    'Bandung':    (3, 3),
    'Cirebon':    (5, 8),
    'Yogyakarta': (8, 1),
    'Semarang':   (8.7, 7.5),
    'Surakarta':  (11, 4),
    'Malang':     (15, 1.5),
    'Surabaya':   (18, 8),
}

G_jawa = nx.Graph()

edges_jawa = [
    ('Jakarta', 'Cirebon', 327),
    ('Jakarta', 'Bandung', 270),
    ('Cirebon', 'Bandung', 120),
    ('Cirebon', 'Semarang', 305),
    ('Bandung', 'Yogyakarta', 373),
    ('Semarang', 'Yogyakarta', 109),
    ('Semarang', 'Surabaya', 369),
    ('Semarang', 'Surakarta', 97),
    ('Yogyakarta', 'Surakarta', 60),
    ('Surakarta', 'Surabaya', 370),
    ('Surabaya', 'Malang', 94),
]

for u, v, w in edges_jawa:
    G_jawa.add_edge(u, v, weight=w)

print("\nElemen pada Graf Jawa:")
print("Node:", G_jawa.nodes())
print("Edge:", G_jawa.edges())

show_graph(G_jawa, pos=pos_jawa, title='Graf Pulau Jawa')

print("\nDFS Graf Jawa:")
i = 1
for u, v in nx.dfs_edges(G_jawa, source='Bandung'):
    print(f"{i}. {u} - {v}")
    i += 1
