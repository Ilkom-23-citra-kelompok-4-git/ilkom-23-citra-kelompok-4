import cv2
import numpy as np
import matplotlib.pyplot as plt

# ======================
# Fungsi Tambahan
# ======================

def print_matrix(citra, x=0, y=0, w=5, h=5, label="Matriks"):
    potongan = citra[y:y+h, x:x+w]
    print(f"\n{label} (dari ({y},{x}), ukuran {h}x{w}):")
    print(np.round(potongan).astype(int))

def cek_koordinat(citra, x, y, label=""):
    try:
        nilai = citra[y, x]
        if hasattr(nilai, 'round'):
            nilai = nilai.round(2)
        print(f"{label} pada koordinat ({y},{x}) = {nilai}")
    except IndexError:
        print(f"Koordinat ({y},{x}) di luar batas gambar.")

# ======================
# Proses Utama
# ======================

# 1. Load gambar grayscale
path = "image/nana.jpeg"  # Ganti dengan path gambar kamu
gambar = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
if gambar is None:
    raise ValueError("Gambar tidak ditemukan. Cek nama file dan path!")

# 2. Histogram Equalization Manual
hist = cv2.calcHist([gambar], [0], None, [256], [0,256]).ravel()
total_pixel = np.sum(hist)
pdf = hist / total_pixel
cdf = np.cumsum(pdf)
gambar_eq = np.round(cdf[gambar] * 255).astype(np.uint8)

# 3. Thresholding
_, gambar_thresh = cv2.threshold(gambar_eq, 127, 255, cv2.THRESH_BINARY)

# 4. Tampilkan hasil
plt.figure(figsize=(12, 4))
plt.subplot(1,3,1); plt.imshow(gambar, cmap='gray'); plt.title("Original")
plt.subplot(1,3,2); plt.imshow(gambar_eq, cmap='gray'); plt.title("Equalized")
plt.subplot(1,3,3); plt.imshow(gambar_thresh, cmap='gray'); plt.title("Thresholded")
plt.tight_layout()
plt.show()

# 5. Print nilai matriks kecil
print_matrix(gambar, x=50, y=50, label="Matriks Asli")
print_matrix(gambar_eq, x=50, y=50, label="Setelah Equalization")
print_matrix(gambar_thresh, x=50, y=50, label="Setelah Thresholding")