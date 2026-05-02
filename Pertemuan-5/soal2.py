'''
2. Diberikan list berisi tuple data mahasiswa dan poin keaktifan: data_aktivitas = [("Diki",
88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
a. Lakukan perulangan pada list tersebut. Jika poin > 80, tampilkan: "[Nama]
mendapatkan predikat Gold". Jika poin 50-80, tampilkan: "[Nama] mendapatkan
predikat Silver". Di bawah itu, tampilkan: "[Nama] mendapatkan predikat Bronze"
'''

data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

for i in data_aktivitas:
    if i[1] > 80:
        print(f"{i[0]} mendapatkan predikat Gold")
    elif i[1] > 50:
        print(f"{i[0]} mendapatkan predikat Silver")
    else:
        print(f"{i[0]} mendapatkan predikat Bronze")