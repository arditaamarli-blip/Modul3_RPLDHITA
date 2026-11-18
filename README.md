# Sistem Manajemen Perpustakaan (MVC Python & MySQL)

## Deskripsi Singkat Aplikasi
Sistem Informasi Manajemen Perpustakaan berbasis Desktop Python menggunakan pola arsitektur **Model-View-Controller (MVC)**. Aplikasi ini dirancang untuk memudahkan pengelolaan data buku, anggota, dan transaksi peminjaman perpustakaan secara terstruktur dengan antarmuka grafis Tkinter serta terhubung ke database MySQL.

## Struktur Direktori MVC
text
Tugas_Modul3/
│
├── config/              # Konfigurasi koneksi database
├── controllers/         # Logika kontroler (penghubung Model & View)
├── models/              # Logika basis data & manipulasi data
├── views/               # Antarmuka pengguna (GUI Tkinter)
├── dist/                # Hasil build aplikasi (.exe)
├── test/                # Kumpulan file unit testing (pytest)
├── main.py              # Titik masuk utama aplikasi (Entry Point)
├── requirements.txt     # Daftar pustaka/dependensi proyek
└── README.md            # Dokumentasi proyek

## Panduan Instalasi & Konfigurasi Database MySQL
1. Pastikan aplikasi **Laragon** sudah terinstal di komputer Anda.
2. Buka Laragon dan klik tombol **Start All** untuk menyalakan layanan **MySQL**.
3. Buat database baru melalui phpMyAdmin atau terminal MySQL dengan nama: `perpustakaan`.
4. Clone atau unduh repositori ini ke komputer lokal Anda.
5. Buka terminal (PowerShell/CMD) di dalam folder proyek, lalu buat dan aktifkan *virtual environment*:
```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
6. Instal seluruh dependensi yang dibutuhkan:
powershell
pip install -r requirements.txt

## Cara Menjalankan Aplikasi
1. Pastikan layanan MySQL di Laragon dalam kondisi aktif.
2. Pastikan *virtual environment* (`.venv`) aktif di terminal VS Code Anda.
3. Jalankan perintah berikut untuk memulai aplikasi:
powershell
python main.py