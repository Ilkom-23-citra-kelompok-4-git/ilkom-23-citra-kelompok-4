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