import heapq  # Digunakan untuk priority queue (inti dari UCS)

# Digunakan untuk fungsi Uniform Cost Search
def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [start])] 
    visited = set()  # Digunakan untuk menyimpan node yang sudah dikunjungi

    while pq:
        # Digunakan untuk mengambil node dengan cost paling kecil
        cost, current_node, path = heapq.heappop(pq)

        if current_node in visited:
            continue  # Digunakan untuk melewati jika sudah dikunjungi

        visited.add(current_node)  # Digunakan menandai sebagai dikunjungi

        # Digunakan untuk menandakan jika sudah sampai tujuan
        if current_node == goal:
            return path, cost

        # Digunakan untuk menambahkan tetangga ke priority queue
        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return None, None  # Jika tidak ada jalur


# Digunakan untuk merepresentasi graf (adjacency list)
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5)],
    'C': [('D', 1), ('E', 6)],
    'D': [('F', 3)],
    'E': [('F', 1)],
    'F': [('G', 2)],
    'G': []
}

# Digunakan untuk menerima input user
start = input("Masukkan gedung awal (start): ").upper()
goal = input("Masukkan gedung tujuan (goal): ").upper()

# Digunakan untuk validasi input
if start not in graph or goal not in graph:
    print("Error: Node tidak ditemukan dalam graf")
else:
    path, cost = uniform_cost_search(graph, start, goal)

    # Digunakan untuk menampilkan output hasil
    if path:
        print("\nJalur terpendek:", " -> ".join(path))
        print("Total cost:", cost)
    else:
        print("Jalur tidak ditemukan")
