import cv2
import numpy as np

# 1. Baca gambar dan pilih region 3x3
image = cv2.imread("bangunan.jpg", cv2.IMREAD_GRAYSCALE)  # Langsung grayscale