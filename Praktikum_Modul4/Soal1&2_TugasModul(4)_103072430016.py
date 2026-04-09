import pandas as pd # Mengimport library
import matplotlib.pyplot as plt
 
data = [ # Menambahkan data sesuai yang ada di grup chat
    ("Budi", 81.24, 73.66, 95.89, 2023),
    ("Siti", 98.52, 84.86, 88.7, 2024),
    ("Asep", 91.96, 71.03, 79.93, 2022),
    ("Dewi", 87.96, 97.28, 71.91, 2024),
    ("Andi", 74.68, 77.76, 79.33, 2023),
    ("Lestari", 74.68, 89.88, 79.76, 2022),
    ("Joko", 71.74, 79.35, 91.89, 2022),
    ("Rina", 95.99, 85.6, 89.13, 2022),
    ("Fajar", 88.03, 86.4, 96.62, 2024),
    ("Indah", 91.24, 75.55, 84.17, 2023),
    ("Agus", 70.62, 99.09, 73.59, 2022),
    ("Fitri", 99.1, 93.25, 91.4, 2022),
    ("Rudi", 94.97, 98.18, 92.82, 2022),
    ("Maya", 76.37, 96.84, 86.84, 2024),
    ("Hadi", 75.45, 87.94, 93.13, 2024),
    ("Sri", 75.5, 97.66, 84.81, 2023),
    ("Wawan", 79.13, 72.65, 85.68, 2024),
    ("Yuni", 85.74, 75.88, 82.83, 2022),
    ("Bambang", 82.96, 71.36, 70.76, 2023),
    ("Ayu", 78.74, 79.76, 73.24, 2022),
]

df = pd.DataFrame(data, columns=["Nama", "Nilai1", "Nilai2", "Nilai3", "Tahun"]) # Digunakan mengubah list menjadi tabel 

summary = df[["Nilai1", "Nilai2", "Nilai3"]].describe().round(2) # Membuat summary sesuai soal 
print(summary) # Menampilkan hasil summary 

plt.figure() # Membuat Box Plot 

plt.boxplot([df["Nilai1"], df["Nilai2"], df["Nilai3"]]) # Membuat box plot dari nilai 1, 2 dan 3 
plt.xticks([1, 2, 3], ["Nilai 1", "Nilai 2", "Nilai 3"])

plt.title("Box Plot Nilai Mahasiswa") 
plt.ylabel("Nilai")
plt.grid()

plt.show()
