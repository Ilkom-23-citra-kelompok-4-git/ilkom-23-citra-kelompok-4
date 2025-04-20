import cv2
import numpy as np
import matplotlib.pyplot as plt

# ================================================
# 1. LOAD GAMBAR EKSTERNAL (MODIFIKASI DI SINI)
# ================================================
def load_image(path):
    # Baca gambar dan konversi ke grayscale
    gambar = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    if gambar is None:
        raise ValueError(f"Gambar di {path} tidak ditemukan!")
    
    # Resize jika terlalu besar (opsional)
    if max(gambar.shape) > 1024:
        print("Resizing gambar...")
        faktor = 1024 / max(gambar.shape)
        gambar = cv2.resize(gambar, (0,0), fx=faktor, fy=faktor)
    
    return gambar

# Ganti dengan path gambar Anda
path_gambar = "bangunan.jpg"  # Contoh: "C:/folder/gambar.jpg"
gambar = load_image(path_gambar)

# ================================================
# 2. TAHAP 1: GAUSSIAN BLUR (PENGHALUSAN)
# ================================================
gambar_blur = cv2.GaussianBlur(gambar, (5, 5), 1)  # Sigma = 1

# ================================================
# 3. TAHAP 2: GRADIEN (OPERATOR SOBEL)
# ================================================
gradien_x = cv2.Sobel(gambar_blur, cv2.CV_64F, 1, 0, ksize=3)  # Gradien horizontal
gradien_y = cv2.Sobel(gambar_blur, cv2.CV_64F, 0, 1, ksize=3)  # Gradien vertikal
magnitudo = np.sqrt(gradien_x**2 + gradien_y**2)  # Kekuatan tepi
arah = np.arctan2(gradien_y, gradien_x) * 180/np.pi  # Arah tepi (derajat)
print("Magnitudo Gradien:", magnitudo[247,805].round(2))
print("Arah Gradien (derajat):", arah[247,805].round(2))