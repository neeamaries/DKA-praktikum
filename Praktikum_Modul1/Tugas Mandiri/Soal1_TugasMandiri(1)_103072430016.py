# Menghitung nilai akhir mahasiswa

nama = input("Nama Mahasiswa : ") # Meminta input nama mahasiswa
tugas = float(input("Nilai Tugas : ")) # Meminta input nilai tugas dan diubah ke float
uts = float(input("Nilai UTS : ")) # Meminta input nilai UTS dan diubah ke float
uas = float(input("Nilai UAS : ")) # Meminta input nilai UAS dan diubah ke float

nilaiAkhir = (tugas * 0.20) + (uts * 0.35) + (uas * 0.45) # Menghitung nilai akhir sesuai ketentuan soal

print("Nama Mahasiswa : ", nama) # Menampilkan output nama mahasiswa
print("Nilai Tugas : ", tugas) # Menampilkan output nilai tugas yang diconvert ke float
print("Nilai UTS : ",uts) # Menampilkan output nilai UTS yang diconvert ke float
print("Nilai UAS : ", uas) # Menampilkan output nilai UAS yang diconvert ke float
print("------------")
print(f"Nilai Akhir : {nilaiAkhir:.2f}") # Menampilkan nilai akhir mahasiswa 
                                         # Menggunakan printf dan .2f untuk menampilkan 2 angka dibelakang koma

    
