import heapq  # Digunakan untuk priority queue (inti UCS)
import networkx as nx  # Digunakan untuk membuat graf
import matplotlib.pyplot as plt  # Digunakan untuk visualisasi

# GRAPH (kota dan jarak)
edges = [
    ("Jakarta", "Cirebon", 327),
    ("Jakarta", "Bandung", 270),
    ("Bandung", "Cirebon", 120),
    ("Bandung", "Yogyakarta", 373),
    ("Cirebon", "Semarang", 305),
    ("Cirebon", "Yogyakarta", 210),
    ("Yogyakarta", "Semarang", 109),
    ("Yogyakarta", "Surakarta", 60),
    ("Semarang", "Surakarta", 97),
    ("Semarang", "Surabaya", 369),
    ("Surakarta", "Malang", 370),
    ("Surabaya", "Malang", 94)
]

# FUNGSI UCS (Uniform Cost Search)
def ucs(edges, start, goal):
    # Digunakan untuk mengubah edges menjadi adjacency list
    graph = {}
    for u, v, w in edges:
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))

    pq = [(0, start, [start])] 
    visited = set()  # Digunakan untuk menyimpan node yang sudah dikunjungi
    expansion = []  # Digunakan untuk menyimpan urutan ekspansi node

    while pq:
        # Digunakan untuk mengambil node dengan cost paling kecil
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue  # Digunakan untuk melewati jika sudah dikunjungi

        visited.add(node)  # Digunakan untuk menandai sebagai dikunjungi
        expansion.append(node)  # Digunakan untuk mencatat urutan ekspansi

        # Digunakan jika tujuan ditemukan
        if node == goal:
            return path, cost, expansion

        # Digunakan untuk menambahkan tetangga ke priority queue
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return None, None, expansion  # Jika tidak ada jalur


# MENJALANKAN UCS
start = "Bandung"
goal = "Malang"

path, cost, expansion = ucs(edges, start, goal)

print("=== HASIL UCS ===")
print("Path:", path)  # Digunakan untuk mengalur tercepat
print("Cost:", cost)  # Digunakan untuk menentukan total biaya
print("Urutan Ekspansi:", expansion)  # Digunakan untuk mengurutkan node dikunjungi


# VISUALISASI GRAF
G = nx.Graph()
G.add_weighted_edges_from(edges)  # Digunakan untuk menambahkan edge ke graf

# Menandai posisi node (biar rapi seperti peta Jawa)
pos = {
    "Jakarta": (0, 3),
    "Bandung": (1, 1),
    "Cirebon": (2, 3),
    "Semarang": (4, 3),
    "Yogyakarta": (4, 1),
    "Surakarta": (5, 2),
    "Surabaya": (7, 3),
    "Malang": (7, 1)
}

plt.figure(figsize=(10,5))
nx.draw(G, pos, with_labels=True, node_size=800)

# Digunakan untuk menampilkan bobot (jarak)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Digunakan untuk membuat highlight jalur hasil UCS
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3)

plt.title("Graf Jawa - UCS Manual")
plt.show()
