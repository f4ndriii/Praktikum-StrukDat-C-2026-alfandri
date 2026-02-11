nilai_siswa = {
"S01": {
    "nama": "Dina",
    "tugas": 80,
    "uts": 75,
    "uas": 85
    },
"S02": {
    "nama": "Abdul Harris",
    "tugas": 90,
    "uts": 88,
    "uas": 92
    },
"S03": {"nama": "Sheila", "tugas": 70, "uts": 65, "uas": 70}
}

#1. Tambahkan data siswa baru: "S04" dengan nama "Fafa", nilai tugas 85, UTS 80, dan UAS 90
nilai_siswa["S04"] = {"nama": "Fafa", "tugas": 85, "uts": 80, "uas": 90}

#2. Hitunglah nilai akhir setiap siswa dengan bobot: (Tugas 20% + UTS 30% + UAS 50%) dan tampilkan hasilnya
for id, data in nilai_siswa.items():
    nama = data["nama"]
    tugas = data["tugas"] * 0.2
    uts = data["uts"] * 0.3
    uas = data["uas"] * 0.5
    nilai_akhir = tugas + uts + uas
    nilai_siswa[id].update({"nilai akhir": nilai_akhir})
    print(f"nama: {nama} | nilai akhir = {nilai_akhir}")

#3. Tampilkan nama siswa yang memiliki nilai UAS di atas 80

for id, data in nilai_siswa.items():
    if data["uas"] > 80:
        print(data["nama"])