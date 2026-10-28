from models.anggota_model import AnggotaModel

model = AnggotaModel()

# CREATE
print("Menambahkan data anggota...")
model.create_anggota("Fika", "Parigi")
model.create_anggota("Cipa", "Makassar")
print("Data anggota berhasil ditambahkan!")

# READ
print("\nData Anggota:")
data = model.read_anggota()

for anggota in data:
    print(anggota)

 