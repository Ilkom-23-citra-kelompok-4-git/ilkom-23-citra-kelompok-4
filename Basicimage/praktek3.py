import cv2
import matplotlib.pyplot as plt

# Baca gambar
image = cv2.imread('D:/MERINDA RISKI/ilkom-23-citra-kelompok-4/Basicimage/th.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Tampilkan gambar asli
plt.figure(figsize=(6, 6))
plt.imshow(image_rgb)
plt.title("Gambar Asli")
plt.axis("off")
plt.show()

# Histogram RGB
colors = ('b', 'g', 'r')
plt.figure()
for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color, label=color.upper())

plt.title("Histogram RGB")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.legend()
plt.show()

# Konversi ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.hist(gray.ravel(), 256, [0, 256], color='gray')
plt.title("Histogram Grayscale")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.show()
