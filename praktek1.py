import cv2

citra = cv2.imread("C:/Users/USER\Documents/Iamfolder/Kuliah/Semester_4/Pengelolaan Citra Digital/Kelompok4-PCD/image/imagekubo.jpg")

# Menampilkan citra digital yang sudah dibaca
# cv2.imshow("KuboShiori1",citra)

# Menunngu hingga user menekan sembarang tombol
# cv2.waitKey()

# [:,:] mengambil semua nilai pixel pada citra (baris kolom)
print("\n=========blue============\n",citra[:,:,0]) #ini adalah chanel blue
print("\n=========green============\n",citra[:,:,1]) #ini adalah chanel green
print("\n=========red============\n",citra[:,:,2]) #ini adalah chanel red