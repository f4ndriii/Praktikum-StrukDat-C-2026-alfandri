#1. Akses dan tampilkan harga barang dari tuple tersebut
barang = ("B001", "Laptop Gaming", 15000000)
print('harga barang = ', barang[2])

#2. Cobalah untuk mengubah harga barang menjadi 14000000. Jelaskan dalam
#komentar kode mengapa hal ini menyebabkan error (Gunakan comment).
'''
barang[2] = 14000000
print(barang[2])
'''
#Terjadi error karena tuple bersifat unchangeable atau tidak dapat diubah

#3. Gunakan teknik unpacking untuk memasukkan isi tuple ke dalam tiga
#variabel: kode, nama, dan harga.
(kode, nama, harga) = barang
print('kode:', kode)
print('nama:', nama)
print('harga:', harga)