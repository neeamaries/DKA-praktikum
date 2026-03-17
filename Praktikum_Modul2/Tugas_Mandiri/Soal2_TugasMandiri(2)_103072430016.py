import numpy as np # Mengimpor library NumPy

nama = [] # Membuat list kosong nama
kode = [] # Membuat list kosong kode
data = [] # Membuat list kosong data

n = int(input("Jumlah Pelanggan : ")) # Meminta user memasukkan jumlah pelanggan

# Menerima Input Data
for i in range(n): # Melakukan perulangan sesuai jumlah pelanggan
    print("\nPelanggan ke-", i+1) # Menampilkan nomor pelanggan yg diinputkan 
    nama.append(input("Nama : ")) # Meminta user memasukkan nama pelanggan 
    belanja = float(input("Total Belanja : ")) # Menerima input total belanja 
    transaksi = int(input("Jumlah Transaksi : ")) # Menerima input jumlah transaksi 

    kodeUndian = np.random.randint(1000, 10000) # Membuat kode secara acak sebanyak 4 digit 

    kode.append(kodeUndian) # Menyimpan kode ke dalam list 
    data.append([belanja, transaksi]) # Menyimpan data belanja dan transaksi dalam satu list 

nilai = np.array(data) # Mengubah list menjadi array NumPy 2 dimensi 
  
# Menampilkan Data Pelanggan 
print("\n=== Data Pelanggan ===")
for i in range(n): # Melakukan perulangan ke semua data 
    print(nama[i], "UND-" + str(kode[i]), [int(nilai[i][0]), int(nilai[i][1])]) # Menampilkan seluruh data tiap pelanggan

# Menampilkan Rata - rata
print("\n=== Rata - Rata ===") 
rataRata = np.mean(nilai[:,0]) # Meghitung rata - rata pada kolom belanja 
print("\nRata - rata Belanja :", int(rataRata)) # Menampilkan rata - rata yang telah dibulatkan 

# Menentukan Pelanggan Prioritas 
print("\n=== Pelanggan Prioritas ===") 
for i in range(n): # Melakukan perulangan sesuai jumlah pelanggan 
    if nilai[i][0] > rataRata: # Jika belanja lebih besar dari rata - rata maka 
        print(nama[i], "UND-" + str(kode[i])) # Akan ditampilkan menjadi pelanggan prioritas 

# Menentukan Peserta & Slot 
peserta = [] # Digunakan untuk membuat list peserta undian

for i in range(n): # Melakukan perulangan sesuai jumlah pelanggan 
    belanja = nilai[i][0] # Mengambil data per pelanggan 
    transaksi = nilai[i][1] # Mengambil data per pelanggan 

    if transaksi >= 3: # Melakukan pengecekan yang memiliki transaksi >= 3 
        if belanja < 300000: # Menentukan slot berdasarkan total belanja 
            slot = 1
        elif belanja <= 700000:
            slot = 2 
        else: 
            slot = 3 
        
        if belanja > rataRata: # Memberikan slot tambahan jika pelanggan prioritas 
            slot += 2 

        for j in range(slot): # Memasukkan index sesuai jumlah slot yang didapatkan
            peserta.append(i)

# Pengundian Pemenang
print("\n=== Pemenang ===")

pesertaUnik = list(set(peserta)) # Menghapus duplikat 

if len(pesertaUnik) >= 2: # Membuat minimal harus ada 2 peserta 
    pemenang = np.random.choice(pesertaUnik, 2, replace=False) # Memilih 2 pemenang secara acak tanpa pengulangan

    for i in pemenang: 
        print(nama[i], "UND-" + str(kode[i])) # Menampilkan pemenang  
else:
    print("Peserta tidak cukup") # Menampilkan pesan jika peserta kurang dari 2 

# Melakukan Pencarian Data
cari = int(input("\nMasukkan kode undian (angka saja): ")) # Meminta kode yang ingin dicari 

ditemukan = False # Sebagai penanda apakah data ditemukan
 
for i in range(n):
    if kode[i] == cari: # Melakukan pengecekkan apakah kode cocok 
        ditemukan = True # Menandakan bahwa kode yg dicari ditemukan 
        print("\nData ditemukan!") # Menampilkan data jikka ditemukan 
        print("Nama :", nama[i])
        print("Kode : UND-" + str(kode[i]))
        print("Belanja :", int(nilai[i][0]))
        print("Transaksi :", int(nilai[i][1]))

if not ditemukan:
    print("Data tidak ditemukan") # Menampilkan pesan jika tidak ditemukan 
