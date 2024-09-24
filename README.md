http://alya-rasheeda-shoptoimpress.pbp.cs.ui.ac.id

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