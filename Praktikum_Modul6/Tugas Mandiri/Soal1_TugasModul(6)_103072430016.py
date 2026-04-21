import networkx as nx # Melakukan import dari library 

G = nx.Graph() # Membuat graph kosong 

edges = [ # Menambahkan edge sesuai ketentuan soal 
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('C', 'G'),
]

G.add_edges_from(edges)

print("DFS tanpa batas : ") # Menampilkan output dari DFS tanpa batas 
i = 1 
for u, v in nx.dfs_edges(G, source='A'): # Melakukan perulangan visiting node yang dimulai dari A
    print(f"{i}. {u} - {v}") # Menampilkan node apa saja yang sudah dikunjungi 
    i += 1 

print("\nDFS dengan depth limit 2 : ") # Menampilkan output dari DFS dengan depth limit 2 
i = 1 
for u, v in nx.dfs_edges(G, source='A', depth_limit=2): # Melakukan perulangan visiting node yang dimulai dari A dan limit depth 2
    print(f"{i}.{u} - {v}") # Menampilkan node apa saja yang sudah dikunjungi 
    i += 1 


