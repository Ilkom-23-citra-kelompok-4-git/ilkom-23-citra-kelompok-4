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