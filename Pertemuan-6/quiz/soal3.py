katalog = [
    {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2}, 
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5}
]

def update_stok(katalog, sn_target, jumlah_tambah):
    for x in katalog:
        if sn_target == x["sn"]:
            x["stok"] = x["stok"] + jumlah_tambah
        else:
            print(">sn tidak ditemukan...")
    pass



for i in range(3):
    sn_target = input("Masukkan sn: ")
    jumlah_tambah = int(input("Masukkan jumlah tambah: "))
    update_stok(katalog, sn_target, jumlah_tambah)

daftar_merk = ()
for x in katalog:
    daftar_merk.add(x["merk"])