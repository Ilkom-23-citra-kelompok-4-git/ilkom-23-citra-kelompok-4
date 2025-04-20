import cv2
import numpy as np

# 1. Baca gambar dan pilih region 3x3
image = cv2.imread("bangunan.jpg", cv2.IMREAD_GRAYSCALE)  # Langsung grayscale
x, y = 805, 247  # Posisi tengah region
print(f"=== Region 3x3 di (x={x}, y={y}) ===")
print("Original Grayscale:\n", image[y-1:y+2, x-1:x+2])

# 2. Gaussian Blur
blurred = cv2.GaussianBlur(image, (5,5), 1)
print("\nGaussian Blur:\n", blurred[y-1:y+2, x-1:x+2].round(1))

# 3. Gradien Sobel
grad_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(grad_x**2 + grad_y**2)
direction = np.arctan2(grad_y, grad_x) * 180/np.pi
print("\nMagnitudo Gradien:\n", magnitude[y-1:y+2, x-1:x+2].round(1))

# 4. Non-Maximum Suppression
def non_max_suppression(mag, angle):
    suppressed = np.zeros_like(mag)
    angle = np.round(angle / 45) * 45  # Quantisasi arah
    
    for i in range(1, mag.shape[0]-1):
        for j in range(1, mag.shape[1]-1):
            # Tetangga berdasarkan arah gradien
            if angle[i,j] == 0:    # Horizontal
            elif angle[i,j] == 90: # Vertikal
            neighbors = [mag[i-1,j], mag[i+1,j]]
                neighbors = [mag[i,j-1], mag[i,j+1]]
