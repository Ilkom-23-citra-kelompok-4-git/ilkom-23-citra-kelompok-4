import cv2
import numpy as np
import matplotlib.pyplot as plt

# ==== Load Gambar Grayscale ====
path = "image/bangunan.jpg"
gambar = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
if gambar is None:
    raise ValueError("Gambar tidak ditemukan. Cek path dan nama file!")