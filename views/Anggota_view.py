import customtkinter as ctk
from tkinter import ttk, messagebox


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("900x500")

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Frame Kiri: Form Data Anggota
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0, column=0, padx=10, pady=10, sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Input Nama Anggota
        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Anggota"
        )
        self.entry_nama.pack(
            pady=10, padx=15, fill="x"
        )

        # Input Alamat
        self.entry_alamat = ctk.CTkTextbox(
            self.frame_kiri,
            height=90
        )
        self.entry_alamat.pack(
            pady=10, padx=15, fill="x"
        )

        # Tombol Simpan
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green",
            command=self.simpan_data
        )
        self.btn_simpan.pack(
            pady=8, padx=15, fill="x"
        )

        # Tombol Update
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data (Update)",
            fg_color="blue",
            command=self.perbarui_data
        )
        self.btn_update.pack(
            pady=8, padx=15, fill="x"
        )

        # Tombol Delete
        self.btn_hapus = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data (Delete)",
            fg_color="red",
            command=self.hapus_data
        )
        self.btn_hapus.pack(
            pady=8, padx=15, fill="x"
        )

        # Tombol Bersihkan Form
        self.btn_bersihkan = ctk.CTkButton(
            self.frame_kiri,
            text="Bersihkan Form",
            fg_color="gray",
            command=self.bersihkan_form
        )
        self.btn_bersihkan.pack(
            pady=8, padx=15, fill="x"
        )

        # Frame Kanan: Tabel Anggota
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0, column=1, padx=10, pady=10, sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Anggota Perpustakaan Ardhita Amarli Putri",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Tabel Data Anggota
        kolom = ("id", "nama", "alamat")

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        self.tabel.column(
            "id", width=50, anchor="center"
        )
        self.tabel.column(
            "nama", width=160
        )
        self.tabel.column(
            "alamat", width=250
        )

        self.tabel.pack(
            fill="both", expand=True, padx=15, pady=10
        )

        # Data contoh untuk tampilan awal
        self.tabel.insert(
            "", "end",
            values=(1, "Andi Pratama", "Jl. Melati No. 12, Palu")
        )
        self.tabel.insert(
            "", "end",
            values=(2, "Siti Nurhaliza", "Jl. Kenanga No. 5, Palu")
        )

        # Memilih baris untuk diedit atau dihapus
        self.tabel.bind(
            "<<TreeviewSelect>>", self.pilih_data
        )

    # Mengosongkan formulir
    def bersihkan_form(self):
        self.entry_nama.delete(0, "end")
        self.entry_alamat.delete("1.0", "end")

    # Mengambil data dari baris terpilih
    def pilih_data(self, event=None):
        pilihan = self.tabel.selection()

        if not pilihan:
            return

        data = self.tabel.item(
            pilihan[0], "values"
        )

        self.bersihkan_form()
        self.entry_nama.insert(0, data[1])
        self.entry_alamat.insert("1.0", data[2])

    # Menyimpan data anggota ke tabel tampilan
    def simpan_data(self):
        nama = self.entry_nama.get().strip()
        alamat = self.entry_alamat.get("1.0", "end").strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama anggota dan alamat harus diisi!"
            )
            return

        id_anggota = max(
            [int(self.tabel.item(i, "values")[0])
             for i in self.tabel.get_children()],
            default=0
        ) + 1

        self.tabel.insert(
            "", "end",
            values=(id_anggota, nama, alamat)
        )

        self.bersihkan_form()
        messagebox.showinfo(
            "Berhasil", "Data anggota berhasil ditambahkan!"
        )

    # Memperbarui data anggota terpilih
    def perbarui_data(self):
        pilihan = self.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota yang ingin diperbarui!"
            )
            return

        nama = self.entry_nama.get().strip()
        alamat = self.entry_alamat.get("1.0", "end").strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama anggota dan alamat harus diisi!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Perbarui data anggota yang dipilih?"
        )

        if konfirmasi:
            data_lama = self.tabel.item(
                pilihan[0], "values"
            )

            self.tabel.item(
                pilihan[0],
                values=(data_lama[0], nama, alamat)
            )

            self.bersihkan_form()
            messagebox.showinfo(
                "Berhasil", "Data anggota berhasil diperbarui!"
            )

    # Menghapus data anggota terpilih
    def hapus_data(self):
        pilihan = self.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota yang ingin dihapus!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Hapus data anggota yang dipilih?"
        )

        if konfirmasi:
            self.tabel.delete(pilihan[0])
            self.bersihkan_form()
            messagebox.showinfo(
                "Berhasil", "Data anggota berhasil dihapus!"
            )


if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()