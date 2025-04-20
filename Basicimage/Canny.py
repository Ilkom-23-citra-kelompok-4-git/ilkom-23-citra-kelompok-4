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
# ================================================
# 4. TAHAP 3: NON-MAXIMUM SUPPRESSION (PENIPISAN TEPI)
# ================================================
def non_max_suppression(magnitudo, arah):
    tepi_tipis = np.zeros_like(magnitudo)
    arah = np.round(arah / 45) * 45  # Bulatkan ke 0°, 45°, 90°, 135°
    
    for i in range(1, magnitudo.shape[0]-1):
        for j in range(1, magnitudo.shape[1]-1):
            # Tetangga berdasarkan arah gradien
            if arah[i,j] == 0 or arah[i,j] == 180:    # Horizontal (Timur-Barat)
                tetangga = [magnitudo[i,j-1], magnitudo[i,j+1]]
            elif arah[i,j] == 45:  # Diagonal 45° (Kanan Atas-Kiri Bawah)
                tetangga = [magnitudo[i-1,j+1], magnitudo[i+1,j-1]]
            elif arah[i,j] == 90:  # Vertikal (Utara-Selatan)
                tetangga = [magnitudo[i-1,j], magnitudo[i+1,j]]
            elif arah[i,j] == 135: # Diagonal 135° (Kiri Atas-Kanan Bawah)
                tetangga = [magnitudo[i-1,j-1], magnitudo[i+1,j+1]]
            else:  # Handle kasus lainnya (jarang terjadi)
                tetangga = []

                # Pertahankan hanya nilai maksimum lokal
            if len(tetangga) > 0 and magnitudo[i,j] >= max(tetangga):
                tepi_tipis[i,j] = magnitudo[i,j]
    return tepi_tipis


tepi_tipis = non_max_suppression(magnitudo, arah)

# ================================================
# 5. TAHAP 4: HYSTERESIS THRESHOLDING (FILTER TEPI)
# ================================================
def hysteresis_threshold(gambar, rendah=30, tinggi=100):
    tepi_kuat = (gambar >= tinggi)
    tepi_lemah = (gambar >= rendah) & (gambar < tinggi)

    # Hubungkan tepi lemah ke tepi kuat
    for i in range(1, gambar.shape[0]-1):
        for j in range(1, gambar.shape[1]-1):
            if tepi_lemah[i,j] and np.any(tepi_kuat[i-1:i+2, j-1:j+2]):
                tepi_kuat[i,j] = True
    return tepi_kuat.astype(np.uint8) * 255

tepi_final = hysteresis_threshold(tepi_tipis, 30, 100)

# ================================================
# 6. TAMPILKAN HASIL SETIAP TAHAP
# ================================================
judul = [
    "1. Gambar Grayscale", 
    "2. Gaussian Blur", 
    "3. Magnitudo Gradien", 
    "4. Non-Max Suppression", 
    "5. Tepi Final (Canny)"
]
hasil = [gambar, gambar_blur, magnitudo, tepi_tipis, tepi_final]

plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(hasil[i], cmap='gray')
    plt.title(judul[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
