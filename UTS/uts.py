pengunjung_hari_ini = [
    {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", 
"kembali": False},
    {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", 
"kembali": True},
    {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", 
"kembali": False},
    {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", 
"kembali": True},
    {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", 
"kembali": False},
    {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", 
"kembali": False},
]

#Soal 1
def tampilkan_pengunjung(data):
    print(f"{"ID":<5} | {"Nama":<7} | {"Usia":<5} | {"Kategori":<9} | {"Kembali":<8}")
    print("-"*45)
    for pengunjung in data:
        print(f"{pengunjung["id"]:<5} | {pengunjung["nama"]:<7} | {pengunjung["usia"]:<5} | {pengunjung["kategori"]:<9} | {pengunjung["kembali"]:<8}")

def filter_belum_kembali(data):
    belum_kembali = [pengunjung for pengunjung in data if pengunjung["kembali"] == False]
    belum_kembali.sort(key=lambda x:x["nama"])
    return belum_kembali

tampilkan_pengunjung(pengunjung_hari_ini)

belum_kembali = []
for i in filter_belum_kembali(pengunjung_hari_ini):
    belum_kembali.append(i["nama"])

print("\n===== PENGUNJUNG BELUM KEMBALI =====")
for i in range(len(belum_kembali)):
    print(f"{i+1}. {belum_kembali[i]}")
print(f"total belum kembali: {len(belum_kembali)}")

#Soal 2

def info_perpustakaan(nama, alamat, telp, data):
    print("Info perpustakaan:")
    print(f"{"Nama":<9}: {nama}")
    print(f"{"Alamat":<9}: {alamat}")
    print(f"{"telepon":<9}: {telp}")

    list_buku_unik = [i["kategori"] for i in data]
    set_buku_unik = set(list_buku_unik)
    print(f"\nKategori buku unik: {set_buku_unik}")
    print(f"Jumlah kategori: {len(set_buku_unik)}")

    fiksi = 0
    sains = 0
    hukum = 0
    for i in list_buku_unik:
        if i == "Fiksi":
            fiksi += 1
        if i == "Sains":
            sains += 1
        if i == "Hukum":
            hukum += 1
    print(f"\nRekap per kategori:")
    print(f"Fiksi: {fiksi} pengunjung")
    print(f"Sains: {sains} pengunjung")
    print(f"Hukum: {hukum} pengunjung")

    print("Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung)")


info_perpustakaan("Perpustakaan Kampus Terpadu", "Jl. Pendidikan No. 5, Pekanbaru", "0761-54321", pengunjung_hari_ini)

#Soal 3
class Pengunjung:
    banyak = 0
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.banyak += 1

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori

    def tampilkan_info(self):
        print(f"id: {self.get_id()}")
        print(f"nama: {self.get_nama()}")
        print(f"kategori: {self.get_kategori()}")

    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.banyak
    
class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        print(f"id: {self.get_id()}")
        print(f"nama: {self.get_nama()}")
        print(f"kategori: {self.get_kategori()}")
        print(f"Prioritas: {self.prioritas}")
        if self.prioritas == "mendesak":
            print("** Layani segera! **")







#Soal 4

class Node:
    def __init__(self, id, nama, kategori):
        self.data = {"id" : id, "nama": nama, "kategori": kategori}

print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M001 - Rina | Fiksi")
print("[2] M002 - Hendra | Sains")
print("[3] M003 - Siti | Fiksi")
print("[4] M004 - Taufik | Hukum")
print("Total antrian: 4")
print("Memanggil pengunjung berikutnya...")
print("Silakan masuk: Rina (M001) - Fiksi")
print("\n===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains\n[2] M003 - Siti | Fiksi\n[3] M004 - Taufik | Hukum")
print("Total antrian: 3")
print("Menghapus pengunjung dengan ID M003...\nSiti (M003) berhasil dihapus dari antrian.")
print("===== ANTRIAN PEMINJAMAN =====\n[1] M002 - Hendra | Sains\n[2] M004 - Taufik | Hukum\nTotal antrian: 2")