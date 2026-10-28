from models.buku_model import BukuModel

model = BukuModel()

def tampilkan_buku(judul_tabel):
    print(f"\n=== {judul_tabel} ===")
    for buku in model.get_all_buku():
        print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")


# 1. Create
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke MySQL!")
tampilkan_buku("Daftar Buku (setelah CREATE)")

# Ambil id buku terakhir yang baru ditambahkan
id_terakhir = model.get_all_buku()[-1]['id_buku']

# 2. Update
print(f"\nMengupdate buku dengan id {id_terakhir}...")
if model.update_buku(id_terakhir,
                     "Pemrograman Python MVC (Revisi)",
                     "Guido van Rossum",
                     2024):
    print("Data berhasil diupdate!")
else:
    print("Gagal update: id tidak ditemukan.")

tampilkan_buku("Daftar Buku (setelah UPDATE)")

# 3. Delete
print(f"\nMenghapus buku dengan id {id_terakhir}...")

if model.delete_buku(id_terakhir):
    print("Data berhasil dihapus!")
else:
    print("Gagal hapus: id tidak ditemukan.")

tampilkan_buku("Daftar Buku (setelah DELETE)")
