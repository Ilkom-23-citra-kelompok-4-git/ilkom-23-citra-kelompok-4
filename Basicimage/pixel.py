import cv2
import numpy as np

# 1. Baca gambar dan pilih region 3x3
image_rgb = cv2.imread("image/bangunan.jpg")  # Baca sebagai BGR
image = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY) 
x, y = 806, 279  # Posisi tengah region
B, G, R = cv2.split(image_rgb)
# print("Original image:\n", image_rgb[y-1:y+2, x-1:x+2])
print(f"=== Region 3x3 di (x={x}, y={y}) ===")
print("Original image:\n")
print("Nilai B channel:\n", B[y-1:y+2, x-1:x+2])
print("Nilai G channel:\n", G[y-1:y+2, x-1:x+2])
print("Nilai R channel:\n", R[y-1:y+2, x-1:x+2])

# image = cv2.imread(image_rgb, cv2.IMREAD_GRAYSCALE)  # Langsung grayscale
print("\nOriginal Grayscale:\n", image[y-1:y+2, x-1:x+2])

# 2. Gaussian Blur
blurred = cv2.GaussianBlur(image, (3,3), 1)
print("\nGaussian Blur:\n", blurred[y-1:y+2, x-1:x+2].round(1))

# 3. Gradien Sobel
grad_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(grad_x**2 + grad_y**2)
direction = np.arctan2(grad_y, grad_x) * 180/np.pi
print("\nMagnitudo Gradien:\n", magnitude[y-1:y+2, x-1:x+2].round(1))
print("Magnitudo Gradien:", magnitude[y,x].round(2))
print("Arah Gradien (derajat):", direction[y,x].round(2))

# 4. Non-Maximum Suppression
def non_max_suppression(mag, angle):
    suppressed = np.zeros_like(mag)
    angle = np.round(angle / 45) * 45  # Quantisasi arah
    
    for i in range(1, mag.shape[0]-1):
        for j in range(1, mag.shape[1]-1):
            # Tetangga berdasarkan arah gradien
            if angle[i,j] == 0:    # Horizontal
                neighbors = [mag[i,j-1], mag[i,j+1]]
            elif angle[i,j] == 90: # Vertikal
                neighbors = [mag[i-1,j], mag[i+1,j]]
            else:                  # Diagonal
                neighbors = [mag[i-1,j-1], mag[i+1,j+1]]
            
            # Pertahankan hanya nilai maksimum lokal
            if mag[i,j] >= max(neighbors):
                suppressed[i,j] = mag[i,j]
    return suppressed

suppressed = non_max_suppression(magnitude, direction)
print("\nNon-Max Suppression:\n", suppressed[y-1:y+2, x-1:x+2].round(1))

# 5. Hysteresis Thresholding (Canny Final)
edges = cv2.Canny(image, 30, 100)  # Versi cepat (tanpa manual thresholding)
print("\nCanny Edge:\n", edges[y-1:y+2, x-1:x+2])