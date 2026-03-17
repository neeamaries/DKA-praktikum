import numpy as np # Mengimpor library NumPy

nama = [] # Membuat list kosong untuk menyimpan nama
data = [] # Membuat list kosong untuk menyimpan nilai 

while True : # Program akan terus berjalan untuk menampilkan menu 
    print("\n=== Menu ===")
    print("1. Input Data Mahasiswa")
    print("2. Tampilkan Nilai Mahasiswa")
    print("3. Tampilkan Nilai Akhir Mahasiswa")
    print("4. Rata - Rata Nilai Mahasiswa")
    print("5. Tampilkan 3 Nilai Tertinggi")
    print("6. Pencarian Data Mahasiswa")
    print("7. Update Data Mahasiswa")
    print("8. Hapus Data Mahasiswa")
    print("9. Keluar")

    pilih = input("Pilih Opsi : ") # Menerima opsi menu yg dipilih oleh user 

    if pilih == "1": # Jika user memilih 1 maka akan masuk ke input nilai mahasiswa
        print("\n=== Input Nilai Mahasiswa ===")
        n = int(input("Jumlah Mahasiswa : ")) # Meminta jumlah mahasiswa yang akan diinputkan
        for i in range(n) : # Melakukan perulangan sesuai jumlah mahasiswa
            print("\nMahasiswa ke-", i+1) 
            nama.append(input("Nama : ")) # Meminta data nama mahasiswa
            tugas = float(input("Tugas : ")) # Meminta data nilai tugas, uas, uts mahasiswa
            uts = float(input("UTS : "))
            uas = float(input("UAS : "))
            data.append([tugas, uts, uas]) # Menyimpan nilai mahasiswa dalam bentuk list 
    
    nilai = np.array(data) # Mengubah list menjadi array NumPy

    if pilih == "2" : # Jika user memilih opsi 2 maka akan menampilkan seluruh nilai mahasiswa
        print("\n=== Menampilkan Seluruh Nilai Mahasiswa ===")
        for i in range(len(nama)): # Melakukan perulangan ke semua mahasiswa
            print(nama[i], nilai[i]) # Menampilkan nama + nilai mahasiswa
    
    if pilih == "3" : # Jika user memilih opsi 3 maka akan menampilkan nilai akhir mahasiswa
        print("\n === Nilai Akhir ===")
        for i in range (len(nama)): # Melakukan perulangan ke semua mahasiswa
            akhir = 0.3 * nilai[i][0] + 0.3 * nilai [i][1] + 0.4 * nilai[i][2] # Menghitung nilai akhir 
            print(nama[i], "=", akhir) # Menampilkan nilai akhir mahasiswa
    
    if pilih == "4": # Jika user memilih opsi 4 maka akan menampilkan nilai rata - rata mahasiswa
        print("\n === Nilai Rata - rata ===")
        total = [] # List untuk menyimpan nilai akhir 
        for i in range (len(nama)):
             akhir = 0.3 * nilai[i][0] + 0.3 * nilai [i][1] + 0.4 * nilai[i][2]
             total.append(akhir) # Menyimpan nilai akhir dari tiap mahasiswa 
        print("Rata - rata : ", np.mean(np.array(total))) # Digunakan untuk menghitung rata - rata semua nilai akhir 

    if pilih == "5": # Jika user memilih opsi 5 maka akan menampilkan 3 nilai tertinggi
        print("\n === 3 Nilai Tertinggi ===")

        total = [] # Menyimpan semua nilai akhir 
        for i in range(len(nama)): 
            akhir = 0.3 * nilai[i][0] + 0.3 * nilai[i][1] + 0.4 * nilai[i][2] # Menghitung nilai akhir 
            total.append(akhir)
    
        urutan = sorted(range(len(total)), key=lambda i: total[i], reverse=True) # Mengurutkan index berdasarkan nilai tertinggi

        for i in urutan[:3]: # Mengambil 3 nilai teratas 
            print(i+1,".",nama[i], "=", total[i]) # Menampilkan ranking 3 mahasiswa
    
    if pilih == "6": # Jika user memilih opsi 6 maka akan mencari data mahasiswa
        print("\n=== Mencari Data Mahasiswa ===")
        cari = input("Cari nama : ") # Meminta input nama yang akan dicari
        for i in range (len(nama)): 
            if cari.lower() in nama[i].lower(): # Pencarian tidak sensitif terhadap huruf besar ataupun kecil
                print(nama[i], nilai[i]) # Menampilkan data jika ditemukan nama yang cocok
    
    if pilih == "7": # Jika user memilih opsi 7 maka akan mengupdate nilai mahasiswa
        print ("\n=== Update Nilai Mahasiswa ===")
        cari = input("Masukkan nama yang ingin di update : ") # Memasukkan nama yang ingin di update
        for i in range (len(nama)) : 
            if cari.lower() in nama[i].lower(): # Melakukan pencarian nama yang cocok seperti yang dicari
                print("Data ditemukan!") # Menandakan bahwa data ditemukan 
                tugas = float(input("Tugas baru : ")) # Memasukkan nilai tugas, uas, dan uts yang baru
                uts = float(input("UTS baru : "))
                uas = float (input("UAS baru : "))
                data[i] = [tugas, uts, uas] # Mengupdate nilai lama dengan nilai yang baru
    
    if pilih == "8": # Jika user memilih opsi 8 maka akan menghapus data mahasiswa
        print("\n === Menghapus Data Mahasiswa ===") 
        cari = input("Masukkan nama yang ini dihapus : ") # Meminta user memasukkan nama yang ingin dihapus
        for i in range(len(nama)): # Melakukan pencarian nama
            if cari.lower() in nama[i].lower(): 
                print("Data berhasil di hapus!") # Menandakan bahwa nama ditemukan dan berhasil dihapus
                nama.pop(i) # Menghapus nama dan data dari list 
                data.pop(i)
                break
    
    if pilih == "9": # Jika user memilih opsi 9 maka akan keluar dari menu ;D 
        break
