http://alya-rasheeda-shoptoimpress.pbp.cs.ui.ac.id

**=================================== TUGAS 4 ===================================**

<!-- Apa perbedaan antara HttpResponseRedirect() dan redirect() -->
    - HttpResponseRedirect() digunakan untuk mengembalikan response redirect secara manual dengan URL spesifik.
    - redirect() adalah shortcut yang menggabungkan HttpResponseRedirect() dengan reverse() untuk mengarahkan URL berdasarkan view name, sehingga lebih ringkas.

<!-- Jelaskan cara kerja penghubungan model Product dengan User! -->
    - Model Product menggunakan relasi ForeignKey untuk menghubungkan setiap produk dengan pengguna (user). Pada ForeignKey, kita menghubungkan Product dengan model User, sehingga setiap produk terkait dengan satu pengguna.

<!-- Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut. -->
    - Authentication: Memverifikasi identitas pengguna (siapa dia), biasanya saat login.
    - Authorization: Menentukan hak akses (apa yang boleh dilakukan pengguna).
    - Django menggunakan authenticate() untuk validasi identitas dan login() untuk autentikasi sesi. Setelah login, Django memanfaatkan middleware untuk mengelola sesi pengguna.

<!-- Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan? -->
    - Django menggunakan sesi dan cookie. Setelah login, cookie dengan sessionid disimpan pada browser klien, yang memungkinkan server mengingat pengguna setiap kali ada request.
    - Kegunaan lain cookies termasuk menyimpan preferensi atau tracking user behavior, tapi tidak semua cookies aman jika tidak dienkripsi atau disalahgunakan.

<!-- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). -->
    - Registrasi, Login, Logout:
    Implementasikan UserCreationForm untuk registrasi, AuthenticationForm untuk login, dan logout() untuk menghapus sesi.
    
    - Buat Dua Akun Pengguna dan Dummy Data:
    Daftarkan dua akun pengguna dan buat tiga dummy data Product untuk masing-masing akun.
    
    - Menghubungkan Product dengan User:
    Gunakan ForeignKey(User) pada model Product untuk menghubungkan setiap produk dengan pengguna.
    
    - Menampilkan Detail Pengguna dan last_login:
    Tambahkan {{ request.user.username }} untuk menampilkan username yang sedang login dan tampilkan last_login dengan menggunakan cookie di halaman utama.

    - Gunakan git add ., git commit -m "<>", dan git push ke repository GitHub.

**=================================== TUGAS 5 ===================================**
 <!-- Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut! -->
    - Inline style (ditulis langsung di elemen HTML) memiliki prioritas tertinggi.
    - ID selector (menggunakan #) memiliki prioritas lebih tinggi dibandingkan class.
    - Class selector (menggunakan .), pseudo-class, dan attribute selector memiliki prioritas lebih rendah dari ID.
    - Element selector memiliki prioritas terendah.

 <!-- Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design! -->
    - Responsive design penting agar tampilan web dapat menyesuaikan di berbagai perangkat seperti desktop, tablet, atau smartphone. Dengan responsive design, pengguna dapat merasakan pengalaman yang optimal di perangkat apa pun.
    - Contoh aplikasi yang sudah menerapkan: Instagram (menyesuaikan di berbagai ukuran layar).
    - Contoh yang belum: Website lama tanpa media query (misalnya situs yang hanya baik dilihat di desktop).

 <!-- Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut! -->
    - Margin: Ruang di luar border elemen, mengatur jarak antar elemen.
    - Border: Garis yang mengelilingi konten dan padding.
    - Padding: Ruang di dalam border, mengatur jarak antara konten dan border.

    - Implementasi:
    .box {
        margin: 20px; /* Memberi jarak di luar elemen */
        border: 2px solid black; /* Memberi garis di sekitar elemen */
        padding: 10px; /* Memberi ruang di dalam elemen */
    }

 <!-- Jelaskan konsep flex box dan grid layout beserta kegunaannya! -->
    - Flexbox: Digunakan untuk membuat layout yang fleksibel dan mengatur elemen di dalam kontainer secara responsif. Cocok untuk layout yang satu dimensi (baris atau kolom).
    - Grid Layout: Digunakan untuk membuat layout yang lebih kompleks dan dua dimensi (baris dan kolom). Berguna untuk struktur halaman yang lebih teratur.
    - Kegunaan:
        - Flexbox: Posisi elemen dalam satu baris atau kolom bisa diatur dengan mudah, misal untuk membuat navbar.
        - Grid: Membuat layout grid yang presisi untuk mengatur konten.

 <!-- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! -->
    - Implementasi Fungsi Hapus dan Edit Product 
        - Buat fungsi `edit_product` dan `delete_product` di `views.py`.
        - Tambahkan path untuk edit dan delete di `urls.py`, agar fitur bisa diakses di halaman.

    - Kustomisasi Halaman Login, Register, dan Tambah Product
        - Gunakan Tailwind untuk membuat halaman login, register, dan tambah product terlihat lebih menarik. Misalnya, gunakan class Tailwind seperti `bg-indigo-600`, `text-white`, dan `rounded-lg` untuk styling tombol dan form.

    - Kustomisasi Halaman Daftar Product 
        - Jika belum ada produk, tampilkan gambar dengan pesan "Product not found" di halaman daftar product.
        - Jika sudah ada produk, tampilkan produk dalam format card yang responsif.

    - Tombol Edit dan Hapus di Setiap Card Product
        - Tambahkan dua tombol di setiap card product: satu untuk edit dan satu untuk delete.
        - Gunakan Tailwind untuk styling tombol dengan class seperti `bg-red-500` untuk edit dan `bg-red-600` untuk delete.

    - Navigation Bar Responsive  
        - Buat navbar yang responsif menggunakan Tailwind. Gunakan class seperti `flex`, `justify-between`, dan `md:hidden` untuk membuat navbar terlihat rapi di mobile dan desktop.