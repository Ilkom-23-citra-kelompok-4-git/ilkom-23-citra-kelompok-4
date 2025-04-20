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

# Jenis-Jenis Edge Dection
1. Sobel: Menggunakan operator konvolusi untuk mendeteksi tepi dengan mempertimbangkan 
perubahan intensitas secara horizontal dan vertikal.
2. Prewitt: Memperkirakan respons maksimum dari sekumpulan kernel konvolusi untuk menemukan 
orientasi tepi lokal untuk setiap elemen piksel 
3.	Roberts: Mendeteksi tepi berdasarkan perbedaan intensitas diagonal antar piksel yang 
berdekatan.
4.	Laplacian of Gaussian (LoG): Operator turunan kedua yang mendeteksi lokasi tepi 
khususnya pada citra tepi yang curam 
5. Canny: Teknik pengolahan citra digital yang populer untuk mengidentifikasi tepi objek dalam gambar 