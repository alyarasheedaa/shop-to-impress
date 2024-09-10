http://alya-rasheeda-shoptoimpress.pbp.cs.ui.ac.id

<!-- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). -->
1. Inisialisasi Repositori Lokal
    - Membuat direktori utama bernama shop-to-impress dan menginisialisasi repositori git di dalamnya

2. Membuat Proyek Django
    - Di dalam direktori utama shop-to-impress menjalankan perintah `django-admin startproject shop-to-impress .` untuk membuat proyek Django dengan direktori `shop-to-impress`

3. Menambahkan Berkas
    - Memastikan berkas `manage.py`, `.gitignore`, dan `requirements.txt` berada di direktori utama sesuai dengan struktur yang diberikan.
   
4. Membuat Virtual Environment
    - Membuat virtual environment dengan menjalankan perintah `python -m venv env` dan mengaktifkannya berdasarkan sistem operasi yang digunakan.
   
5. Membuat Aplikasi
    - Membuat aplikasi `main` dengan menjalankan perintah `python manage.py startapp main` di dalam direktori utama `shop-to-impress`.

6. Mendaftarkan Aplikasi
    - Membuka berkas `settings.py` di dalam direktori `shop-to-impress` dan menambahkan aplikasi `main` ke dalam daftar `INSTALLED_APPS`.

7. Menambahkan URL Routing
    - Membuat berkas `urls.py` di dalam aplikasi `main` dan menghubungkannya dengan berkas `urls.py` di proyek dengan menggunakan fungsi `include`.

8. Membuat Template HTML
    - Membuat direktori `templates` di dalam aplikasi `main` dan menambahkan berkas `main.html`

9. Membuat Model
    - Menambahkan model di dalam berkas `models.py` pada aplikasi `main`, melakukan migrasi model dengan perintah `makemigrations` dan `migrate`.

10. Menghubungkan Views dengan Template
    - Menghubungkan views dan template di `views.py` dengan menggunakan fungsi `render` untuk me-render template dengan data yang diambil dari model.

11. Push Git
    - Menambahkan dan meng-commit semua perubahan ke repositori lokal, lalu push ke repositori github.

<!-- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. -->

Client ---- Request ----> urls.py (Routing URL)
                            |
                            v
                      views.py (Mengolah Request)
                            |
                            v
                     models.py (Akses Data dari Database)
                            |
                            v
                  templates (HTML Response)
                            |
                            v
Client <---- Response ------

- urls.py: Berkas ini mengatur rute URL, menentukan permintaan mana yang harus diarahkan ke fungsi view tertentu.
- views.py: Fungsi view menerima permintaan dari urls.py, mengolahnya, dan mengakses data melalui model jika diperlukan.
- models.py: Model digunakan untuk mendefinisikan dan mengakses data dari database. Django secara otomatis mengubahnya menjadi query SQL melalui ORM.
- Template HTML: Setelah data diproses oleh views, views mengembalikan data yang diolah kepada template HTML untuk ditampilkan kepada pengguna.

<!-- Jelaskan fungsi git dalam pengembangan perangkat lunak! -->
Git berfungsi sebagai sistem kontrol versi yang memungkinkan pengembang untuk:
    - Melacak perubahan kode: Setiap perubahan yang dibuat pada proyek dapat dilacak dan di-commit, membuat versi sebelumnya tetap tersedia.
    - Kolaborasi: Git memfasilitasi kolaborasi antar anggota tim dengan memungkinkan beberapa pengembang bekerja di berbagai fitur atau bug tanpa bentrok.
    - Revisi kode: Jika ada kesalahan, pengembang dapat dengan mudah mengembalikan proyek ke versi sebelumnya yang stabil.
    - Branching: Fitur branching pada Git memungkinkan pengembang untuk mengerjakan fitur baru atau memperbaiki bug di cabang yang terpisah tanpa mengganggu kode utama.

<!-- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? -->
Framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena:
    - Pemahaman Arsitektur MVT: Django menggunakan konsep Model-View-Template (MVT) yang memisahkan logika bisnis, tampilan, dan data, memberikan pemahaman dasar yang baik dalam pengembangan aplikasi web.
    - Keteraturan dan Produktivitas: Django memiliki fitur bawaan yang lengkap seperti ORM, routing URL, validasi formulir, dan pengelolaan pengguna yang memudahkan dalam pengembangan cepat (rapid development).
    - Scalability: Django cocok untuk aplikasi kecil hingga besar, belajar membangun aplikasi yang scalable.
    - Komunitas dan Dokumentasi: Django memiliki komunitas yang besar dan dokumentasi yang lengkap sehingga mudah dipelajari oleh pemula.

<!-- Mengapa model pada Django disebut sebagai ORM? -->
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan teknik ORM untuk menghubungkan objek dalam kode Python dengan tabel di database relasional. ORM memungkinkan pengembang untuk bekerja dengan basis data menggunakan objek Python, tanpa harus menulis query SQL secara langsung. ORM pada Django otomatis menerjemahkan operasi pada model menjadi query SQL yang relevan, sehingga mempermudah pengelolaan database.