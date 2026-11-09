import tkinter as tk
from tkinter import ttk, messagebox

PRODI = [
    "Teknik Informatika",
    "Sistem Informasi",
    "Teknik Industri",
    "Manajemen",
    "Akuntansi",
    "Pendidikan Guru Sekolah Dasar",
]

KEGIATAN = [
    "Seminar Teknologi",
    "Workshop Pemrograman",
    "Lomba Futsal",
    "Bakti Sosial",
    "Pelatihan Kepemimpinan",
]


class AplikasiPendaftaran(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pendaftaran Kegiatan Mahasiswa")
        self.geometry("760x640")
        self.minsize(720, 600)

        # Variabel kontrol
        self.var_nama = tk.StringVar()
        self.var_nim = tk.StringVar()
        self.var_prodi = tk.StringVar()
        self.var_gender = tk.StringVar(value="Laki-laki")
        self.var_kegiatan = {k: tk.BooleanVar() for k in KEGIATAN}

        self._buat_menu()
        self._buat_form()
        self._buat_area_info()

        # Event keyboard: Enter menjalankan Submit, Escape menjalankan Reset
        self.bind("<Return>", self.submit)
        self.bind("<Escape>", lambda e: self.reset())
        self.entry_nama.focus()

    # ------------------------------------------------------------------ Menu
    def _buat_menu(self):
        menubar = tk.Menu(self)

        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Reset", command=self.reset)
        menu_file.add_separator()
        menu_file.add_command(label="Keluar", command=self.keluar, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=menu_file)

        menu_bantuan = tk.Menu(menubar, tearoff=0)
        menu_bantuan.add_command(label="About", command=self.tampilkan_about)
        menubar.add_cascade(label="Bantuan", menu=menu_bantuan)

        self.config(menu=menubar)
        self.bind("<Control-q>", lambda e: self.keluar())

    # ------------------------------------------------------------------ Form
    def _buat_form(self):
        frame_form = ttk.LabelFrame(self, text="Formulir Pendaftaran", padding=10)
        frame_form.pack(fill="x", padx=12, pady=(12, 6))
        frame_form.columnconfigure(1, weight=1)

        # Nama (Entry)
        ttk.Label(frame_form, text="Nama").grid(row=0, column=0, sticky="w", pady=4)
        self.entry_nama = ttk.Entry(frame_form, textvariable=self.var_nama)
        self.entry_nama.grid(row=0, column=1, sticky="ew", pady=4)

        # NIM (Entry, hanya menerima angka)
        ttk.Label(frame_form, text="NIM").grid(row=1, column=0, sticky="w", pady=4)
        vcmd = (self.register(self._hanya_angka), "%P")
        self.entry_nim = ttk.Entry(
            frame_form, textvariable=self.var_nim,
            validate="key", validatecommand=vcmd,
        )
        self.entry_nim.grid(row=1, column=1, sticky="ew", pady=4)

        # Program studi (Combobox)
        ttk.Label(frame_form, text="Program Studi").grid(row=2, column=0, sticky="w", pady=4)
        self.combo_prodi = ttk.Combobox(
            frame_form, textvariable=self.var_prodi, values=PRODI, state="readonly"
        )
        self.combo_prodi.grid(row=2, column=1, sticky="ew", pady=4)
        self.combo_prodi.set("-- Pilih Program Studi --")

        # Jenis kelamin (Radiobutton)
        ttk.Label(frame_form, text="Jenis Kelamin").grid(row=3, column=0, sticky="w", pady=4)
        frame_gender = ttk.Frame(frame_form)
        frame_gender.grid(row=3, column=1, sticky="w", pady=4)
        for teks in ("Laki-laki", "Perempuan"):
            ttk.Radiobutton(
                frame_gender, text=teks, value=teks, variable=self.var_gender
            ).pack(side="left", padx=(0, 15))

        # Kegiatan (Checkbutton) + Listbox pilihan terpilih
        ttk.Label(frame_form, text="Kegiatan").grid(row=4, column=0, sticky="nw", pady=4)
        frame_kegiatan = ttk.Frame(frame_form)
        frame_kegiatan.grid(row=4, column=1, sticky="ew", pady=4)
        frame_kegiatan.columnconfigure(1, weight=1)

        frame_cek = ttk.Frame(frame_kegiatan)
        frame_cek.grid(row=0, column=0, sticky="nw")
        for k in KEGIATAN:
            ttk.Checkbutton(
                frame_cek, text=k, variable=self.var_kegiatan[k],
                command=self.perbarui_listbox,
            ).pack(anchor="w")

        frame_list = ttk.Frame(frame_kegiatan)
        frame_list.grid(row=0, column=1, sticky="nsew", padx=(20, 0))
        ttk.Label(frame_list, text="Kegiatan yang dipilih:").pack(anchor="w")
        self.listbox = tk.Listbox(frame_list, height=5)
        self.listbox.pack(fill="x")

        # Alasan (Text)
        ttk.Label(frame_form, text="Alasan Mengikuti").grid(row=5, column=0, sticky="nw", pady=4)
        frame_alasan = ttk.Frame(frame_form)
        frame_alasan.grid(row=5, column=1, sticky="ew", pady=4)
        self.text_alasan = tk.Text(frame_alasan, height=4, wrap="word")
        scroll = ttk.Scrollbar(frame_alasan, command=self.text_alasan.yview)
        self.text_alasan.config(yscrollcommand=scroll.set)
        self.text_alasan.pack(side="left", fill="x", expand=True)
        scroll.pack(side="right", fill="y")
        # Enter di Text harus membuat baris baru, bukan Submit
        self.text_alasan.bind("<Return>", lambda e: e.widget.insert("insert", "\n") or "break")

        # Tombol
        frame_tombol = ttk.Frame(frame_form)
        frame_tombol.grid(row=6, column=0, columnspan=2, pady=(10, 0))
        ttk.Button(frame_tombol, text="Submit", command=self.submit).pack(side="left", padx=5)
        ttk.Button(frame_tombol, text="Reset", command=self.reset).pack(side="left", padx=5)

    # ------------------------------------------------------------ Area info
    def _buat_area_info(self):
        frame_info = ttk.LabelFrame(self, text="Ringkasan Pendaftaran", padding=10)
        frame_info.pack(fill="both", expand=True, padx=12, pady=(6, 12))

        self.text_info = tk.Text(frame_info, height=8, state="disabled", wrap="word",
                                 background="#f4f4f4")
        self.text_info.pack(fill="both", expand=True)

    def _tulis_info(self, teks):
        self.text_info.config(state="normal")
        self.text_info.delete("1.0", "end")
        self.text_info.insert("1.0", teks)
        self.text_info.config(state="disabled")

    # -------------------------------------------------------------- Handler
    @staticmethod
    def _hanya_angka(isi_baru):
        """Dipanggil tiap ketikan: izinkan hanya digit (maks. 15 karakter)."""
        return isi_baru == "" or (isi_baru.isdigit() and len(isi_baru) <= 15)

    def perbarui_listbox(self):
        """Tampilkan kegiatan yang dicentang pada Listbox."""
        self.listbox.delete(0, "end")
        for k in KEGIATAN:
            if self.var_kegiatan[k].get():
                self.listbox.insert("end", k)

    def submit(self, event=None):
        nama = self.var_nama.get().strip()
        nim = self.var_nim.get().strip()
        prodi = self.var_prodi.get()
        gender = self.var_gender.get()
        kegiatan = [k for k in KEGIATAN if self.var_kegiatan[k].get()]
        alasan = self.text_alasan.get("1.0", "end").strip()

        # Validasi
        if not nama:
            messagebox.showwarning("Validasi", "Nama tidak boleh kosong!")
            self.entry_nama.focus()
            return
        if not nim:
            messagebox.showwarning("Validasi", "NIM tidak boleh kosong!")
            self.entry_nim.focus()
            return
        if len(nim) < 8:
            messagebox.showwarning("Validasi", "NIM minimal 8 digit angka!")
            self.entry_nim.focus()
            return
        if prodi not in PRODI:
            messagebox.showwarning("Validasi", "Silakan pilih program studi!")
            return
        if not kegiatan:
            messagebox.showwarning("Validasi", "Pilih minimal satu kegiatan!")
            return

        ringkasan = (
            f"Nama           : {nama}\n"
            f"NIM            : {nim}\n"
            f"Program Studi  : {prodi}\n"
            f"Jenis Kelamin  : {gender}\n"
            f"Kegiatan       : {', '.join(kegiatan)}\n"
            f"Alasan         : {alasan if alasan else '-'}\n"
        )
        self._tulis_info(ringkasan)
        messagebox.showinfo("Berhasil", f"Pendaftaran {nama} (NIM {nim}) berhasil!")

    def reset(self):
        self.var_nama.set("")
        self.var_nim.set("")
        self.combo_prodi.set("-- Pilih Program Studi --")
        self.var_gender.set("Laki-laki")
        for var in self.var_kegiatan.values():
            var.set(False)
        self.listbox.delete(0, "end")
        self.text_alasan.delete("1.0", "end")
        self._tulis_info("")
        self.entry_nama.focus()

    def tampilkan_about(self):
        about = tk.Toplevel(self)
        about.title("About")
        about.geometry("340x180")
        about.resizable(False, False)
        about.transient(self)
        about.grab_set()

        ttk.Label(about, text="Pendaftaran Kegiatan Mahasiswa",
                  font=("Arial", 13, "bold")).pack(pady=(20, 5))
        ttk.Label(about, text="Praktikum Tkinter Sesi 11\nAdvanced Widgets dan Event Handling",
                  justify="center").pack(pady=5)
        ttk.Label(about, text="Versi 1.0").pack(pady=5)
        ttk.Button(about, text="Tutup", command=about.destroy).pack(pady=10)

    def keluar(self):
        if messagebox.askyesno("Keluar", "Apakah Anda yakin ingin keluar?"):
            self.destroy()


if __name__ == "__main__":
    AplikasiPendaftaran().mainloop()
