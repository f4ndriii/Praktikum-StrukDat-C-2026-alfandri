stok_gadget = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
]

batas_atas = int(input("Masukkan batas atas: "))
batas_bawah = int(input("Masukkan batas bawah: "))

def filter_harga(data, min_harga, max_harga):
    list = []
    for x in data:
        if x.get("harga") >= min_harga and x.get("harga") <= max_harga:
            list.append(x)
    return list
if filter_harga(stok_gadget, batas_bawah, batas_atas) == []:
    print("\n>Tidak ada gadget dalam rentang harga tersebut...")
else:
    print("\nDaftar Hp")
    print("=========================")
    for i in filter_harga(stok_gadget, batas_bawah, batas_atas):
        print(f"Merek   :   {i.get("merk")}")
        print(f"Tipe    :   {i.get("tipe")}")
        print(f"Harga   :   {i.get("harga")}\n")