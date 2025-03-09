import cv2

citra = cv2.imread("C:/Users/USER\Documents/Iamfolder/Kuliah/Semester_4/Pengelolaan Citra Digital/Kelompok4-PCD/image/imagekubo.jpg")

# Menampilkan citra digital yang sudah dibaca
cv2.imshow("KuboShiori1",citra)

# Menunngu hingga user menekan sembarang tombol
cv2.waitKey()