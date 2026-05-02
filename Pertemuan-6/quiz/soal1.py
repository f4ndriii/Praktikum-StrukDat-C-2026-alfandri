produk = []

def registrasi_gadget(merk, tipe, harga, sn):
    if harga >= 1000000 and len(sn) >= 5:
        dict = {
            "merk" : merk,
            "tipe" : tipe,
            "harga" : harga,
            "sn" : sn,
            "status" : "Tersedia"
        }
        return dict
    else:
        print("Input tidak valid...")
        return False

for i in range(2):
    print("\nMasukkan produk baru...\n======================================")
    merk = input("Masukkan merk: ")
    tipe = input("Masukkan tipe: ")
    harga = float(input("Masukkan harga: "))
    sn = input("Masukkan sn: ")

    if registrasi_gadget(merk, tipe, harga, sn):
        produk.append(registrasi_gadget(merk, tipe, harga, sn))

x = 1
list_produk = list(produk)
for dict in produk:
    print("\n===============================================================")
    print(f"Produk {x}")
    print(f"merk   : {dict["merk"]}")
    print(f"tipe   : {dict["tipe"]}")
    print(f"harga  : {dict["harga"]}")
    print(f"sn     : {dict["sn"]}")
    print(f"status : {dict["status"]}")
    print("===============================================================")
    x += 1