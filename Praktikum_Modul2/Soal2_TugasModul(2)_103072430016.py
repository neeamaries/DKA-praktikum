import numpy as np # Mengimpor library NumPy

n = int(input("Masukkan jumlah barang : ")) # Meminta input jumlah barang ke user 

nama = [] # Membuat list kosong untuk nama
kode = [] # Membuat list kosong untuk kode barang
jumlah = [] # Membuat list kosong untuk jumlah 
harga = [] # Membuat list kosong untuk harga 

for i in range(n) : # Melakukan perulangan sesuai jumlah barang 
    print("\nData barang ke-", i+1) # Menampilkan urutan barang yang akan dimasukkan datanya
    nama.append(input("Nama Barang : ")) # Meminta input nama dan dimasukkan ke list nama 
    kode.append(input("Kode Barang : ")) # Meminta input kode barang dan dimasukkan ke list kode barang 
    jumlah.append(int(input("Jumlah : "))) # Meminta input jumlah dan dimasukkan ke list jumlah 
    harga.append(float(input("Harga per unit : "))) # Meminta input harga per unit dan dimasukkan ke list harga 

harga_np = np.array(harga) # Mengubah list harga dan jumlah menjadi array NumPy
jumlah_np = np.array(jumlah)

print("\n === Data Inventaris ===") # Menampilkan data yang sudah didapatkan 
totalSemua = 0  # Digunakan untuk menyimpan seluurh nilai inventaris 

for i in range(n) : # Perulangan untuk menampilkan seluruh data barang 
    total = jumlah[i] * harga [i] # Menghitung total harga per barang 
    totalSemua += total # Menambahkan total tiap barang ke total keseluruhan 
    print("Nama = ",nama[i],"; Kode = ", kode[i],"; Jumlah = ", jumlah[i],"; Harga = ", f"{harga[i]:.0f}", "; Total= ", f"{total:.0f}") # Menampilkan data seluruh barang yang didapatkan

print("\nTotal Nilai Inventaris: ", f"{totalSemua:.0f}") # Menampilkan total seluruh nilai inventaris

cari = input ("\nPencarian barang (Nama / Kode) : ") # Meminta input user barang yang akan dicari 

for i in range(n) : # Melakukan perulangan untuk pengecekan barang 
    if cari.lower() in nama[i].lower() or cari in kode[i]: # Kondisi pengecekan jika sama maka akan di print baris berikutnya
        print("\n === Data Ditemukan! ===") # Menampilkan pesan jika barang ditemukan
        print("Nama : ", nama[i]) # Menampilkan detail barang yang ditemukan 
        print("Kode : ", kode[i])
        print("Jumlah : ", jumlah[i])
        print("Harga : ", f"{harga[i]:.0f}")
        print("Total : ", f"{jumlah[i] * harga[i]:.0f}")
