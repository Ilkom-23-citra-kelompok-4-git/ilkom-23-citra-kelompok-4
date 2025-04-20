# Pengertian Edge Detection 
Edge detection adalah teknik dalam pengolahan citra digital yang digunakan untuk menemukan
batas-batas (tepi) dari objek yang ada dalam gambar. Tepi biasanya merupakan tempat 
terjadinya perubahan intensitas warna atau kecerahan yang tajam.

# Tujuan Edge Detection
1. Menemukan Bentuk dan Kontur Objek
Deteksi tepi sangat penting untuk mengidentifikasi bentuk dan struktur dari objek-objek yang ada
dalam gambar. Dengan menyoroti perbedaan intensitas piksel yang mencolok, metode ini dapat
menampilkan garis-garis batas yang membentuk kontur objek. Hasilnya, kita bisa mengetahui ukuran,
bentuk, serta posisi objek dengan lebih mudah dan akurat, tanpa perlu memproses seluruh isi gambar
secara menyeluruh.
2. Mengurangi Jumlah Data Citra untuk Proses Selanjutnya
Edge detection membantu menyederhanakan gambar dengan hanya menampilkan informasi penting berupa garis tepi. Hal ini secara otomatis mengurangi jumlah data yang harus diproses oleh sistem, terutama untuk tahap selanjutnya seperti segmentasi citra, pelacakan objek, atau klasifikasi gambar. Dengan demikian, proses komputasi menjadi lebih efisien dan cepat tanpa kehilangan informasi penting dari gambar.
3. Dengan mendeteksi tepi-tepi yang ada, kita bisa memahami bagaimana struktur atau susunan elemen dalam gambar tersebut. Ini sangat berguna untuk berbagai aplikasi, misalnya dalam analisis citra medis untuk
melihat struktur organ tubuh, dalam pemetaan untuk mengenali batas-batas wilayah, atau dalam visi komputer untuk membantu robot mengenali lingkungan sekitarnya. Informasi struktur ini juga bisa menjadi dasar untuk proses rekonstruksi objek 3D dari citra 2D.

# Metode Canny terdiri dari lima tahapan utama, yaitu:
1. Grayscale adalah format gambar yang hanya terdiri dari warna abu-abu, 
tanpa warna lain seperti merah, hijau, atau biru. Setiap piksel dalam gambar grayscale 
memiliki nilai intensitas dari hitam (0) ke putih (255).
2. Gaussian Blur adalah metode menghaluskan gambar dengan menerapkan filter Gaussian untuk 
mengurangi noise dan detail kecil. Ini berguna sebelum deteksi tepi, agar hasil tepinya 
lebih halus dan akurat.