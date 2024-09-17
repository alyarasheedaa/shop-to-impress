http://alya-rasheeda-shoptoimpress.pbp.cs.ui.ac.id

<!-- Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? -->
    - Data delivery penting untuk memastikan pertukaran informasi antara server dan client berjalan lancar dan sesuai format yang diharapkan. Ini mendukung fungsionalitas platform secara efisien.

<!-- Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? -->
    - JSON lebih baik karena lebih ringan, mudah dibaca, dan cepat diproses. JSON lebih populer dibandingkan XML karena strukturnya sederhana, cocok untuk API modern, dan lebih mendukung aplikasi web.

<!-- Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? -->
    - Method ini digunakan untuk memeriksa apakah data yang diinput ke dalam form sesuai dengan aturan validasi yang ditetapkan. Kita butuh method ini agar bisa memastikan data yang diterima form sudah valid sebelum diproses lebih lanjut, misalnya disimpan ke database.

<!-- Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? -->
    - csrf_token melindungi dari serangan CSRF. Tanpa token ini, penyerang bisa mengirim permintaan berbahaya atas nama pengguna. Token memastikan permintaan berasal dari sumber yang sah.

<!-- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). -->
    - Buat file forms.py di dalam direktori main untuk membuat form input data menggunakan ModelForm. Tambahkan form yang menghubungkan ke model yang sudah ada, yaitu MoodEntry.

    - Di views.py, buat dua view baru: show_xml dan show_json untuk menampilkan semua data MoodEntry dalam format XML dan JSON menggunakan serializers. Untuk ID-based views, tambahkan dua view lagi: show_xml_by_id dan show_json_by_id. Ini memungkinkan pengambilan data berdasarkan ID spesifik dari database.

    - Tambahkan URL pattern di urls.py untuk setiap view baru agar setiap endpoint akan terhubung ke view yang sesuai.

    - Mengakses URL menggunakan Postman: Uji keempat URL yang sudah diimplementasi menggunakan Postman.

    - Add-commit-push ke GitHub: 
    git add .
    git commit -m "tugas 3"
    git push origin main
    Pastikan semua perubahan sudah ter-push.
 
URL POSTMAN -> https://drive.google.com/drive/folders/1Lvs748AmCG43wxLcCzoZE7LNp77wND8P?usp=sharing
