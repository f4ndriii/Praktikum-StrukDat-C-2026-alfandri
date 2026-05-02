tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

#1. Tentukan keahlian yang dimiliki oleh kedua tim (irisan)
keahlian_kedua_tim = tim_frontend & tim_backend
print(keahlian_kedua_tim)

#2. Tentukan keahlian yang hanya dimiliki oleh tim_backend
hanya_backend = tim_backend - tim_frontend
print(hanya_backend)

#3. Gabungkan kedua set tersebut untuk melihat daftar total keahlian unik yang tersedia di perusahaan
gabungan = tim_frontend | tim_backend
print(gabungan)