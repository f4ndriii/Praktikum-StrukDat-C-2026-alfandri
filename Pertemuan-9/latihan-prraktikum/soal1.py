'''
Parkir Dua Arah — Penelusuran Maju & Mundur
Sistem parkir bertingkat ingin bisa menelusuri kendaraan dari depan ke
belakang dan dari belakang ke  depan, karena petugas bisa berada di kedua
ujung. 

Tugas: 
1. Buat struktur Node dan DoubleLinkedList dengan pointer next dan prev.
2. Buat fungsi tambah_kendaraan(plat) untuk menambah kendaraan ke akhir list.
3. Buat fungsi tampilkan_maju() untuk mencetak semua kendaraan dari head ke tail.
4. Buat fungsi tampilkan_mundur() untuk mencetak semua kendaraan dari tail ke head.
'''

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        baru = Node(plat)
        # Jika list kosong
        if not self.head:
            self.head = baru
            self.tail = baru
        # Masukkan di akhir list
        else:
            baru.prev = self.tail
            self.tail.next = baru
            self.tail = baru

    def tampilkan_maju(self):
        # Jika list kosong
        if not self.head:
            print("List kosong...")
            return
        # Mulai dari head/depan
        p = self.head
        while p:
            print(p.data)
            # Setiap perulangan maju
            p = p.next

    def tampilkan_mundur(self):
        # Jika list kosong
        if not self.head:
            print("List kosong...")
            return
        # Mulai dari tail/belakang
        q = self.tail
        while q:
            print(q.data)
            # Setiap perulangan mundur
            q = q.prev

parkir_list = DoubleLinkedList()
parkir_list.tambah_kendaraan("B 1234 ABC")
parkir_list.tambah_kendaraan("D 5678 XYZ")
parkir_list.tambah_kendaraan("A 9999 TUV")

print("[Maju]")
parkir_list.tampilkan_maju()
print("\n[Mundur]")
parkir_list.tampilkan_mundur()