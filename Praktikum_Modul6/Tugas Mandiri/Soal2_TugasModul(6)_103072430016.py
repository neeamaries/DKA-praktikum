import networkx as nx # Melakukan import dari library 

G = nx.Graph() # Membuat Graph kosong 

edges = [ # Menambahkan edge sesuai ketentuan soal 
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('C', 'G'),
]

G.add_edges_from(edges)

print ("DFS traversal : ") 

goal = 'F' # Melakukan set goal yang akan dicapai 
found = False # Membuat kondisi false diawal 

for u, v in nx.dfs_edges(G, source='A'): # Melakukan perulangan yang menunjungi tiap node dimulai dari A
    print (f"{u} -> {v}") # Menampilkan node yang dikunjungi 

    if v == goal: # Membuat permisalan jika v mencapai goal 
        found = True # Mengubah kondisi menjadi true jika mencapai goal 

if found: 
    print("\nNode F dapat dicapai dari A menggunakan DFS.") # Menampilkan pesan ini jika mencapai goal 
else: 
    print("\nNode F tidak ditemukan. ") # Menampilkan pesan ini jika goal tidak ditemukan 



    
