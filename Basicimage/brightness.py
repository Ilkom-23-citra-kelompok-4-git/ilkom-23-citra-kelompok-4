import cv2
import numpy as np
import matplotlib.pyplot as plt

# ==== Load Gambar Grayscale ====
path = "image/bangunan.jpg"
gambar = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
if gambar is None:
    raise ValueError("Gambar tidak ditemukan. Cek path dan nama file!")

# ==== Brightness Adjustment ====
nilai_tambah = 50  # kamu bisa ubah ke -50 juga untuk menggelapkan
gambar_terang = cv2.add(gambar, nilai_tambah)

# ==== Visualisasi ====
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1); plt.imshow(gambar, cmap='gray'); plt.title("Original")
plt.subplot(1, 2, 2); plt.imshow(gambar_terang, cmap='gray'); plt.title(f"Brightness +{nilai_tambah}")
plt.tight_layout()
plt.show()

# ==== Cek Nilai Pixel (Opsional) ====
y, x = 52, 52
print(f"Original pixel ({y},{x}):", gambar[y, x])
print(f"After brightness +{nilai_tambah}:", gambar_terang[y, x])