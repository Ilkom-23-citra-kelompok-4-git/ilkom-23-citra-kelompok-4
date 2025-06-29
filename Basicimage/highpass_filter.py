import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Baca gambar dalam grayscale
img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Cek apakah gambar berhasil dibaca
if img is None:
    print("Gambar tidak ditemukan. Pastikan file 'image.png' ada di folder yang sama.")
    exit()

# 2. Definisikan kernel high-pass (Laplacian)
kernel_high_pass = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# 3. Terapkan konvolusi untuk high-pass filtering
high_pass_result = cv2.filter2D(img, -1, kernel_high_pass)

# 4. Tampilkan cuplikan matriks 3x3 dari posisi (50, 50)
row, col = 10, 10  # kamu bisa ubah ini ke posisi lain

print("Patch 3x3 dari gambar asli (posisi 10,10):")
print(img[row:row+3, col:col+3])

print("\nPatch 3x3 dari hasil high-pass filter (posisi 10,10):")
print(high_pass_result[row:row+3, col:col+3])

# 5. Tampilkan hasil gambar
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Gambar Asli (Grayscale)")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Hasil High-Pass Filter")
plt.imshow(high_pass_result, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
