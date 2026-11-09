# Praktikum Tkinter Sesi 11 - Pendaftaran Kegiatan Mahasiswa

## Nama: Akrom Turikul Huda
## NIM: 2595114001

## Tujuan
Membangun aplikasi GUI menggunakan Python Tkinter dengan memanfaatkan berbagai widget,
event handling, validasi input, menu, dan dialog.

## Fitur
- **Entry** untuk nama, dengan validasi agar tidak boleh kosong.
- **Entry** untuk NIM: hanya menerima angka (maks. 15 digit), wajib diisi, minimal 8 digit.
- **Combobox** untuk memilih program studi.
- **Radiobutton** untuk memilih jenis kelamin.
- **Checkbutton** untuk memilih kegiatan, dan **Listbox** yang menampilkan kegiatan terpilih.
- **Text** untuk alasan mengikuti kegiatan.
- Tombol **Submit** dan **Reset**.
- Ringkasan pendaftaran pada area informasi.
- **Messagebox** untuk notifikasi (peringatan validasi, sukses, konfirmasi keluar).
- Menu **File** (Reset, Keluar) dan menu **Bantuan** (About).
- Jendela **About** menggunakan **Toplevel**.
- Event keyboard: `Enter` = Submit, `Esc` = Reset, `Ctrl+Q` = Keluar.
- Tata letak dengan **Frame** dan geometry manager `pack` dan `grid`.

## Cara Menjalankan
1. Pastikan Python 3 terpasang (Tkinter sudah termasuk pada instalasi standar).
   Di Linux: `sudo apt install python3-tk`.
2. Jalankan:
   ```
   python main.py
   ```

## Struktur Repository
```
praktikum-tkinter-sesi-11/
├── main.py
├── README.md
└── screenshots/
```
