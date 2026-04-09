import networkx as nx # Melakukan import dari library 
import matplotlib.pyplot as plt # Melakukan import dari library dan membuat alias

WG = nx.Graph() # Membuat graph kosong untuk graph berbobot 

WG.add_weighted_edges_from([ # Menambahkan edge pada grapf beserta bobotnya 
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2)
])

pos = nx.spring_layout(WG, seed=42) # Membuat visualisasi graph dari yang telah dibuat 
nx.draw(WG, pos, with_labels=True, node_color='gray', node_size=1500, font_size=12)
labels = nx.get_edge_attributes(WG, 'weight')
nx.draw_networkx_edge_labels(WG, pos, edge_labels=labels)
plt.show()

# Digunakan untuk menghitung jalur terpendek menggunakan library networkx
shortest_path = nx.shortest_path(WG, source='A', target='E', weight='weight') 

# Digunakan untuk menghitung total bobot dari jalur yang ditemukan
shortest_distance = nx.shortest_path_length(WG, source='A', target='E', weight='weight')

print("Jalur terpendek dari A ke E:", shortest_path) # Digunakan untuk menampilkan jalur terpendek yang didapatkan 
print("Total bobot:", shortest_distance) # Digunakan untuk menampilkan total bobot dari jalur tersebut 
