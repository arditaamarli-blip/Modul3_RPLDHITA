import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

# ARDHITA AMARLI PUTRI F5212530109
class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Binding tombol
        self.view.title(f"Sistem Manajemen Perpustkaan - Mode: {self.user_role.upper()}")
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        self.view.btn_hapus.configure(
            command=self.hapus_buku
        )

        self.view.btn_update.configure(
            command=self.update_buku
        )
        
        # OTORISASI: Jika bukan admin, nonaktifkan form input dan tombol simpan
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text= "Akses Terkunci (khusus admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Memuat data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Menghapus isi tabel lama
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari database
        data_buku = self.model.get_all_buku()

        # Menampilkan data ke tabel
        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def simpan_data(self):
        # Proteksi ganda di level controller
        if self.user_role !="admin":
            messagebox.showeror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        berhasil = self.model.create_buku(
            judul,
            penulis,
            tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat menyimpan data."
            )

    def hapus_buku(self):
        selected = self.view.tabel.focus()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data yang ingin dihapus!"
            )
            return

        data = self.view.tabel.item(selected, "values")
        id_buku = data[0]

        berhasil = self.model.delete_buku(id_buku)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )
            self.muat_data_tabel()

    def update_buku(self):
        selected = self.view.tabel.focus()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data yang ingin diperbarui!"
            )
            return

        data = self.view.tabel.item(selected, "values")
        id_buku = data[0]

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        berhasil = self.model.update_buku(
            id_buku,
            judul,
            penulis,
            tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )
            self.muat_data_tabel()

    # Menjalankan aplikasi
    def run(self):
        self.view.mainloop()
