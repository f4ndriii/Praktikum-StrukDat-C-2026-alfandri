'''
4. Diberikan data produk dalam bentuk list of dictionaries:
gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]
a. Tambahkan satu key baru bernama "kategori" dengan nilai "Aksesoris" untuk produk
Keyboard.
b. Tambahkan satu item baru: "Headset" dengan harga 350000 dan stok 8.
c. Hitung Total Nilai Aset (Harga x Stok) untuk setiap item. Tampilkan output dengan
format:
Item: [Nama] | Total Aset: Rp [Hasil Perkalian]
'''

gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]

#a
gudang_pc[1]["Kategori"] = "Aksesoris"

#b
gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8})

#c
for i in range(len(gudang_pc)):
    print(f"item: {gudang_pc[i]["item"]}|Total aset: {gudang_pc[i]["harga"] * gudang_pc[i]["stok"]}")
