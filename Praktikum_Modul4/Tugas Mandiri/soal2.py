import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(__file__)
df2 = pd.read_csv(os.path.join(base_dir, "soal2.csv"))

plt.figure(figsize=(14, 6))

# Membuat Histogram
plt.subplot(1, 2, 1)
plt.hist(df2['math score'], bins=15, alpha=0.6, label='Math Score')
plt.hist(df2['reading score'], bins=15, alpha=0.6, label='Reading Score')
plt.title('Distribusi Nilai Matematika dan Membaca')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.legend()

# Membuat Box Plot
plt.subplot(1, 2, 2)
plt.boxplot(
    [df2['math score'], df2['reading score']],
    labels=['Math Score', 'Reading Score'],
    patch_artist=True,
    widths=0.5,
    boxprops=dict(facecolor='lightgray', color='black', linewidth=1.5),
    medianprops=dict(color='black', linewidth=2),
    whiskerprops=dict(color='black', linewidth=1.5),
    capprops=dict(color='black', linewidth=1.5),
    flierprops=dict(marker='o', markerfacecolor='gray', markersize=5, linestyle='none', markeredgecolor='black')
)
plt.title('Perbandingan Distribusi Nilai')
plt.ylabel('Nilai')

plt.tight_layout()
plt.show()


