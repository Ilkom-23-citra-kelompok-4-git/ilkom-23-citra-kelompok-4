import cv2

# 1. Baca gambar
image = cv2.imread("bangunan.jpg")
citragray = cv2.imread("bangunan.jpg", cv2.IMREAD_GRAYSCALE)

# 2. Fungsi untuk handle klik mouse
def capture_region(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
        region = citragray[y-1:y+2, x-1:x+2]  # Ambil 3x3 pixels
        print(f"\nRegion 3x3 di (x={x}, y={y}):")
        print(region)

        # Tampilkan visual
        marked = citragray.copy()
        cv2.rectangle(marked, (x-1,y-1), (x+1,y+1), (0,255,0), 1)  # Kotak hijau
        cv2.imshow("Image", marked)


  # 3. Tampilkan gambar dan set callback
cv2.imshow("Image gray", citragray)
cv2.setMouseCallback("Image gray", capture_region)
cv2.waitKey(0)
cv2.destroyAllWindows()
