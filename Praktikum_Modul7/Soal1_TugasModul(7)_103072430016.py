import heapq  # Digunakan untuk priority queue (UCS)
import networkx as nx  # Digunakan untuk membuat dan mengelola graf
import matplotlib.pyplot as plt  # Digunakan untuk visualisasi graf

# GRAPH (data kota dan jarak)
edges = [
    ("Arad", "Zerind", 75), ("Arad", "Timisoara", 118), ("Arad", "Sibiu", 140),
    ("Zerind", "Oradea", 71), ("Oradea", "Sibiu", 151),
    ("Sibiu", "Fagaras", 99), ("Sibiu", "Rimnicu Vilcea", 80),
    ("Rimnicu Vilcea", "Pitesti", 97), ("Rimnicu Vilcea", "Craiova", 146),
    ("Pitesti", "Bucharest", 101), ("Fagaras", "Bucharest", 211),
    ("Timisoara", "Lugoj", 111), ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75), ("Drobeta", "Craiova", 120),
    ("Craiova", "Pitesti", 138),
    ("Bucharest", "Giurgiu", 90), ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98), ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142), ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87)
]

# FUNGSI UCS (Uniform Cost Search)
def ucs(edges, start, goal):
    # Mengubah edge list menjadi adjacency list
    graph = {}
    for u, v, w in edges:
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))

    pq = [(0, start, [start])] 
    visited = set()  # Digunakan untuk menyimpan node yang sudah dikunjungi
    expansion_order = []  # Digunakan untuk menyimpan urutan ekspansi

    while pq:
        cost, node, path = heapq.heappop(pq)  # Mengambil node dengan cost terkecil

        if node in visited:
            continue  # Melewati jika sudah dikunjungi

        visited.add(node)  # Menandai node sebagai dikunjungi
        expansion_order.append(node)  # Mencatat urutan ekspansi

        if node == goal:
            return path, cost, expansion_order  # Apabila goal ditemukan

        # Menambahkan tetangga ke priority queue
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return None, None, expansion_order  # Jika tidak ada jalur ditemukan 


# MENJALANKAN UCS
start = "Arad"
goal = "Bucharest"

path, cost, expansion = ucs(edges, start, goal)

print("=== HASIL UCS MANUAL ===")
print("Path:", path)  # Digunakan untuk alur terpendek
print("Cost:", cost)  # Digunakan untuk menghitung total biaya
print("Urutan Ekspansi:", expansion)  # Digunakan untuk urutan node dikunjungi


# VISUALISASI GRAF
G = nx.Graph()
G.add_weighted_edges_from(edges)  #Digunakan untuk menambahkan edge ke graf

pos = nx.spring_layout(G, seed=42)  # Digunakan untuk mengatur posisi node

plt.figure(figsize=(12,8))
nx.draw(G, pos, with_labels=True, node_size=700)  # Digunakan untuk menggambar graf

# Menampilkan bobot pada edge
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Membuat highlight jalur hasil UCS
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3)

plt.title("UCS Manual (Bukan Dijkstra Built-in)")
plt.show()
