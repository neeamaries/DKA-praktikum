import heapq  # Digunakan untuk menentukanpriority queue

# FUNGSI MENAMPILKAN GRAF
def display_graph(graph):
    print("\n=== DAFTAR RUTE ===")
    total_edges = 0
    for kota, tetangga in graph.items():  # Digunakan untuk loop setiap kota
        for tujuan, biaya in tetangga:  # Digunakan untuk loop tetangga kota
            print(f"{kota} -> {tujuan} : Rp {biaya}.000")
            total_edges += 1  # Digunakan untuk menghitung jumlah rute

    print(f"\nTotal kota   : {len(graph)}")  # Digunakan untuk menentukan jumlah node
    print(f"Total rute   : {total_edges}")  # Digunakan untuk menentukan jumlah edge


# FUNGSI UCS (Uniform Cost Search)
def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()  # Digunakan untuk menyimpan node yang sudah dikunjungi
    visited_order = []  # Digunakan untuk menyimpan urutan node dikunjungi
    expansion_order = []  # Digunakan untuk menyimpan urutan ekspansi node

    while pq:
        # Digunakan untuk mengambil node dengan cost terkecil
        cost, current_node, path = heapq.heappop(pq)

        if current_node in visited:
            continue  # Digunakan untuk melewati jika sudah dikunjungi

        visited.add(current_node)  # Digunakan untuk menandai node
        visited_order.append(current_node)  # Digunakan untuk mencatat node dikunjungi
        expansion_order.append(current_node)  # Digunakan untuk mencatat ekspansi

        # Digunakan untuk menandai jika tujuan ditemukan
        if current_node == goal:
            return path, cost, visited_order, expansion_order

        # Digunkaan untuk menambahkan tetangga ke priority queue
        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return None, None, visited_order, expansion_order 


# GRAPH (Representasi kota & biaya)
graph = {
    'Jakarta': [('Bandung', 150), ('Cirebon', 250)],
    'Bandung': [('Jakarta', 150), ('Cirebon', 100), ('Yogyakarta', 400)],
    'Cirebon': [('Jakarta', 250), ('Bandung', 100), ('Semarang', 280), ('Yogyakarta', 200)],
    'Semarang': [('Cirebon', 280), ('Yogyakarta', 120), ('Surabaya', 350)],
    'Yogyakarta': [('Bandung', 400), ('Cirebon', 200), ('Semarang', 120), ('Surabaya', 380)],
    'Surabaya': [('Semarang', 350), ('Yogyakarta', 380), ('Malang', 90)],
    'Malang': [('Surabaya', 90)]
}

# MENAMPILKAN GRAF
display_graph(graph)

# INPUT USER
start = input("\nMasukkan kota asal: ").title()
goal = input("Masukkan kota tujuan: ").title()

# PROSES UCS
if start not in graph or goal not in graph:
    print("Error: Kota tidak ditemukan")
else:
    path, cost, visited, expansion = uniform_cost_search(graph, start, goal)

    print("\n=== HASIL UCS ===")

    if path:
        print("Jalur terbaik       :", " -> ".join(path))  # Digunakan untuk menentukan jalur tercepat
        print(f"Total biaya         : Rp {cost}.000")  # Digunakan untuk menentukan total biaya

        print("\nDetail perjalanan:")
        for i in range(len(path)-1):
            print(f"{path[i]} -> {path[i+1]}")  # Digunakan untuk menentukan langkah perjalanan

    else:
        print("Jalur tidak ditemukan")

    print("\nNode dikunjungi     :", visited)  #Digunkana untuk menandai semua node yang dikunjungi
    print("Jumlah dikunjungi   :", len(visited))  #Digunkaan untuk menghitung jumlah node dikunjungi
    print("Urutan ekspansi     :", expansion)  # Urutan proses UCS
