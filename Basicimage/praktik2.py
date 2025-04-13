import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
img = cv2.imread('gambar.jpg')  # ganti dengan nama file gambarmu
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # ubah ke RGB biar warnanya benar di matplotlib

# 1. Mean Filter
mean = cv2.blur(img, (9, 9))  # kernel 3x3

# 2. Median Filter
median = cv2.medianBlur(img, 9)  # kernel size = 3

# 3. Gaussian Blur
gaussian = cv2.GaussianBlur(img, (9, 9), 0)  # kernel 3x3, sigmaX = 0 (otomatis)