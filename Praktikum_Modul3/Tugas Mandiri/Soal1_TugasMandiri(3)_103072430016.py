import networkx as nx # Melakukan import dari library 
import matplotlib.pyplot as plt # Melakukan import dari library dan menambahkan alias

G = nx.Graph() # Digunakan untuk membuat graph tak berarah

G.add_nodes_from(['A', 'B', 'C', 'D', 'E']) # Menambahkan node pada graph yg telah dibuat 

G.add_edges_from([ # Menambahkan edge pada graph
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E')
])

print("Node:", G.nodes()) # Digunakan untuk menampilkan node 
print("Edge:", G.edges()) # Digunakan untuk menampilkan edge 

pos = nx.spring_layout(G, seed=42) # Merupakan visualisasi dari graph yg telah dibuat 
nx.draw(G, pos, with_labels=True, node_color='gray', node_size=1500, font_size=12)
plt.title("Graf Soal 1")
plt.show()

print("Degree setiap node:")
for node, degree in G.degree(): # Menggunakan perulangan untuk menentukan jumlah degree dari setiap node 
    print(f"{node}: {degree}")

print("\nNeighbor dari node D:")
print(list(G.neighbors('D'))) # Digunakan untuk menentukan neighbor dari node D

