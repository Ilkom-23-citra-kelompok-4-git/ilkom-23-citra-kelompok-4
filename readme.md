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
memiliki nilai intensitas dari hitam (0) ke putih (255). Nilai ini merepresentasikan
seberapa terang atau gelap sebuah piksel. Gambar dalam format grayscale sering digunakan
dalam pemrosesan citra digital karena lebih sederhana dan lebih efisien dibandingkan gambar
berwarna, namun tetap mampu menyampaikan informasi visual yang cukup jelas, terutama untuk
analisis bentuk, tekstur, atau pola.
2. Gaussian Blur adalah metode menghaluskan gambar dengan menerapkan filter Gaussian untuk 
mengurangi noise dan detail kecil. Ini berguna sebelum deteksi tepi, agar hasil tepinya 
lebih halus dan akurat. Filter ini menggunakan fungsi distribusi Gaussian untuk menghitung nilai rata-rata dari piksel-piksel di sekitarnya, sehingga menghasilkan efek blur yang lebih alami dan menyebar merata.
3. Gradien adalah ukuran perubahan intensitas warna atau kecerahan antar piksel dalam suatu 
gambar. Gradien menunjukkan seberapa cepat atau tajam perubahan tersebut terjadi dan arah 
perubahannya. Pada tahap perhitungan gradien, kami menggunakan operator Sobel untuk 
menghitung perubahan intensitas piksel secara horizontal dan vertikal. Setelah mendapatkan 
gradien horizontal (Gx) dan vertikal (Gy), selanjutnya dilakukan perhitungan magnitudo dan 
arah gradien. Operator Sobel bekerja dengan mengonvolusi gambar menggunakan kernel khusus, 
sehingga dapat mendeteksi tepi secara lebih halus dan akurat dibanding metode sederhana.
4. Non-Maximum Suppression adalah proses menghilangkan piksel yang tidak berada di sepanjang 
tepi yang paling kuat, hanya mempertahankan piksel dengan nilai gradien tertinggi dalam arah 
gradien. Setelah menghitung gradien, arah gradien diambil untuk setiap piksel. piksel dengan 
nilai gradien tertinggi dipertahankan, sementara yang lebih rendah akan dihapus. Sehingga 
menghasilkan gambar yang memiliki tepi lebih tajam dan lebih terdefinisi. 
5. Hysteresis Thresholding adalah proses pemilihan tepi dengan menggunakan dua nilai ambang 
yaitu, tepi kuat dan tepi lemah. Piksel dianggap sebagai bagian dari tepi hanya jika mereka 
terhubung dengan piksel tepi kuat. Piksel yang memiliki gradien di antara kedua ambang 
dianggap tepi lemah. Tepi lemah hanya dianggap sebagai tepi jika terhubung ke tepi kuat. 
Jika tidak, maka dihapus. Piksel tepi lemah yang terhubung ke tepi kuat dipertahankan 
sebagai bagian dari tepi.
