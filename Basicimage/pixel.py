import cv2
import numpy as np

# 1. Baca gambar dan pilih region 3x3
image = cv2.imread("bangunan.jpg", cv2.IMREAD_GRAYSCALE)  # Langsung grayscale
x, y = 805, 247  # Posisi tengah region
print(f"=== Region 3x3 di (x={x}, y={y}) ===")
print("Original Grayscale:\n", image[y-1:y+2, x-1:x+2])