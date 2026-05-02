'''
Case: Layanan Valet VIP tetap memungkinkan kendaraan untuk menyalip.
Namun, karena keterbatasan sistem (Singly Linked List), petugas hanya bisa
melihat kendaraan di depannya. Kendaraan VIP baru dapat disisipkan tepat di
belakang kendaraan VIP tertentu yang sudah ada dalam antrean. Karena hanya
satu arah, untuk pengecekan urutan, petugas harus membacanya dari kendaraan
paling depan hingga paling belakang.

a. Tugas:
1. Gunakan struktur Singly Linked List (hanya memiliki pointer next).
2. Buat fungsi sisipkan_vip(plat_baru, plat_target):
Mencari plat_target dalam antrean, lalu menyisipkan
plat_baru tepat setelahnya.
3. Buat fungsi tampilkan_antrean() untuk menunjukkan urutan
kendaraan dari depan ke belakang.
b. Logika: Menelusuri list dari head untuk mencari plat_target. Setelah
ditemukan, buat node baru, hubungkan next dari node baru ke next milik
target, lalu ubah next milik target ke node baru.
'''

class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None

    def tambah_kendaraan(self, plat):
        # Logika: Mencari node terakhir dari 'self' saat ini
        currentNode = self
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = Node(plat)
        print(f"Kendaraan {plat} ditambahkan.")

    def sisipkan_vip(self, plat_baru, plat_target):
        currentNode = self
        while currentNode is not None and currentNode.plat != plat_target:
            currentNode = currentNode.next

        if currentNode is None:
            print(f"Target {plat_target} tidak ditemukan.")
            return

        baru = Node(plat_baru)
        baru.next = currentNode.next
        currentNode.next = baru
        print(f"Kendaraan VIP {plat_baru} disisipkan setelah {plat_target}.")

    def tampilkan_antrean(self):
        currentNode = self
        urutan = []
        while currentNode:
            urutan.append(f"[{currentNode.plat}]")
            currentNode = currentNode.next
        print("Antrean:", " -> ".join(urutan))

antrean = Node("B 1234 ABC")

antrean.tambah_kendaraan("D 8888 XYZ")
antrean.tambah_kendaraan("B 2022 EFG")
antrean.tampilkan_antrean()

antrean.sisipkan_vip("VIP 0001 AAA", "D 8888 XYZ")
antrean.tampilkan_antrean()

antrean.sisipkan_vip("VIP 0002 BBB", "B 1234 ABC")
antrean.tampilkan_antrean()