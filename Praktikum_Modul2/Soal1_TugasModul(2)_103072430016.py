import numpy as np # Digunakan untuk mengimpor library NumPy

n = int(input("Masukkan jumlah mahasiswa : ")) # Meminta input jumlah mahasiswa ke user 

nama = [] # Membuat list kosong untuk nama 
nim = [] # Membuat list kosong untuk nim
nilai = [] # Membuat list kosong untuk nilai
tahun = [] # Membuat list kosong untuk tahun masuk

for i in range(n) : # Melakukan perulangan sesuai jumlah mahasiswa 
    print("\nData Mahasiswa ke-", i+1) # Menampilkan urutan mahasiswa yang akan dimasukkan datanya
    nama.append(input("Nama : ")) # Meminta input nama dan dimasukkan ke list nama 
    nim.append(input("NIM : ")) # Meminta input nim dan dimasukkan ke list nim 
    nilai.append(float(input("Nilai : "))) # Meminta input nilai dan dimasukkan ke list nilai
    tahun.append(int(input("Tahun Masuk : "))) # Meminta input tahun dan dimasukkan ke list tahun masuk

nilai_np = np.array(nilai) # Mengubah list nilai menjadi array NumPy 
 
print("\n === Data Mahasiswa === ") # Menampilkan output data mahasiswa yang didapat
for i in range (n): # Melakukan perulangan sesuai data mahasiswa yang diterima
    print("Siswa ke",i+1,"; Nama = ", nama[i],"; NIM = ", nim[i], "; Nilai = ", nilai[i],"; Tahun Masuk = ", tahun[i]) # Menampilkan seluruh data mahasiswa

print("\nNilai Tertinggi : ", np.max(nilai_np)) # Menampilkan nilai terbesar menggunakan fungsi np.max
print("Nilai Terendah : ", np.min(nilai_np)) # Menampilkan nilai terkecil menggunakan np.min
print("Nilai Rata - rata : ", np.mean(nilai_np)) # Menghitung rata - rata menggunakan np.mean

cariMahasiswa = input("\nPencarian Mahasiswa Berdasarkan NIM / Nama : ") # Meminta input untuk mahasiswa yang dicari

for i in range (n) : # Loop untuk pengecekan data mahasiswa
    if cariMahasiswa == nama[i] or cariMahasiswa == nim[i] : # Pengecekkan apakah input sama seperti data yang sudah ada
        print("\n === Nama ditemukan! === ") # Pesan akan ditampilkan jika sudah ditemukan
        print("Nama : ", nama[i]) # Menampilkan data mahasiswa yang cocok dengan pencarian 
        print("NIM : ", nim[i])
        print("Nilai : ", nilai[i])
        print("Tahun Masuk : ", tahun[i]) 
