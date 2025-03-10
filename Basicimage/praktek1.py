import cv2
# Membaca citra digital pada komputer
citra = cv2.imread("C:/Users/USER\Documents/Iamfolder/Kuliah/Semester_4/Pengelolaan Citra Digital/Kelompok4-PCD/image/imagekubo.jpg")

# Menampilkan citra digital yang sudah dibaca
cv2.imshow("KuboShiori",citra)
cv2.imshow("KuboShiori-blue",citra[:,:,0]) #menampilkan citra blue
cv2.imshow("KuboShiori-green",citra[:,:,1]) #menampilkan citra green
cv2.imshow("KuboShiori-red",citra[:,:,2]) #menampilkan citra red

# [:,:] mengambil semua nilai pixel pada citra (baris kolom)
print("\n=========blue============\n",citra[:,:,0]) #menampilkan chanel blue
print("\n=========green============\n",citra[:,:,1]) #menampilkan chanel green
print("\n=========red============\n",citra[:,:,2]) #menampilkan chanel red
print("\n=========semua chanel============\n",citra) #menampilkan semua chanel 

# Menunngu hingga user menekan sembarang tombol
cv2.waitKey()
