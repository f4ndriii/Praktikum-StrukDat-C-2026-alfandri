from kurs import kurs
from konverter import idr_to_asing, asing_to_idr
from tabulate import tabulate

data = []

for key in kurs:
    baris = []
    baris.append(key)
    baris.append(kurs[key])
    data.append(baris)

print(tabulate(data, headers=["Mata Uang", "Kurs (Rupiah)"]))
print("----------------------------")
print("Pilih arah konversi:")
print("1. IDR ke mata uang asing")
print("2. Mata uang asing ke IDR\n")

pilihan = input("Pilihan: ")



match pilihan:

    case "1":
        jumlah = int(input("Masukkan jumlah uang: "))
        mata_uang = input("Masukkan kode mata uang tujuan: ").upper()
        if mata_uang == "USD" or "EUR" or "SGD" or "JPY":
            print(f"Nilainya dalam {mata_uang} adalah {idr_to_asing(jumlah, mata_uang):,} {mata_uang}")
        else:
            print("Mata uang tidak tersedia")

    case "2":
        mata_uang = input("Masukkan kode mata uang asal: ").upper()
        if mata_uang == "USD" or "EUR" or "SGD" or "JPY":
            jumlah = int(input("Masukkan jumlah uang: "))
            print(f"Nilainya dalam IDR adalah Rp.{asing_to_idr(jumlah, mata_uang):,}")
        else:
            print("Mata uang tidak tersedia")

    case _:
        print("Pilihan tidak valid...")

