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