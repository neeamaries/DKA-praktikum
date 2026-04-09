import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(__file__)
df1 = pd.read_csv(os.path.join(base_dir, "soal1.csv")) # Mengambil data dari soal1.csv

grouped = df1.groupby(['Pclass', 'Sex']).size().unstack() # Digunakan untuk menghitung penumpang per kelas berdasarkan gender

age_not_survived = df1[df1['Survived'] == 0]['Age'].dropna() # Mengambil data usia berdasarkan status selamat
age_survived = df1[df1['Survived'] == 1]['Age'].dropna()

fig1, axes = plt.subplots(1, 2, figsize=(14, 6))

# Pembuatan Bar Plot
grouped.plot(kind='bar', ax=axes[0])
axes[0].set_title('Jumlah Penumpang Titanic per Kelas dan Gender')
axes[0].set_xlabel('Pclass')
axes[0].set_ylabel('Jumlah Penumpang')
axes[0].legend(title='Sex')
axes[0].tick_params(axis='x', rotation=0) 

# Pembuatan Box Plot
axes[1].boxplot(
    [age_not_survived, age_survived],
    labels=['Tidak Selamat', 'Selamat'],
    patch_artist=True,
    widths=0.5,
    boxprops=dict(facecolor='lightgray', color='black', linewidth=1.5),
    medianprops=dict(color='black', linewidth=2),
    whiskerprops=dict(color='black', linewidth=1.5),
    capprops=dict(color='black', linewidth=1.5),
    flierprops=dict(marker='o', markerfacecolor='gray', markersize=5, linestyle='none', markeredgecolor='black')
)
axes[1].set_title('Distribusi Usia Berdasarkan Status Selamat')
axes[1].set_xlabel('Status Selamat')
axes[1].set_ylabel('Usia')

plt.tight_layout()
plt.show()

