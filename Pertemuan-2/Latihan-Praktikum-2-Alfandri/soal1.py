stok = [15, 50, 30, 25, 40]

#1. Tambahkan stok baru sebesar 100 ke akhir list
stok.append(100)
print(stok)

#2. Sisipkan angka 75 di posisi indeks ke-2
stok.insert(2, 75)
print(stok)

#3. Urutkan list tersebut dari yang terbesar ke terkecil
stok.sort()
print(stok)

#4. Hitunglah nilai rata-rata dari seluruh stok tersebut
jumlah = 0
banyak = 0
for x in stok:
    jumlah = jumlah + x
    banyak = banyak + 1
rata_rata = jumlah/banyak
print('rata-rata =', rata_rata)

#5. Tampilkan isi list setelah semua perubahan dilakukan
print(stok)