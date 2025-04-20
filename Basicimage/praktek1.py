import cv2
# Membaca citra digital pada komputer
citra = cv2.imread("bangunan.jpg")

# Menampilkan citra digital yang sudah dibaca
cv2.imshow("Bangunan",citra)
cv2.imshow("Bangunan-blue",citra[:,:,0]) #menampilkan citra blue
cv2.imshow("Bangunan-green",citra[:,:,1]) #menampilkan citra green
cv2.imshow("Bangunan-red",citra[:,:,2]) #menampilkan citra red

# [:,:] mengambil semua nilai pixel pada citra (baris kolom)
print("\n=========blue============\n",citra[:,:,0]) #menampilkan chanel blue
print("\n=========green============\n",citra[:,:,1]) #menampilkan chanel green
print("\n=========red============\n",citra[:,:,2]) #menampilkan chanel red
print("\n=========semua chanel============\n",citra) #menampilkan semua chanel 

# Menunngu hingga user menekan sembarang tombol
cv2.waitKey()
