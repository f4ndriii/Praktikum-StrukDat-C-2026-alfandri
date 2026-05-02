'''
Case: Kendaraan yang sudah selesai urusan harus keluar melalui satu pintu yang
sama. Karena ini antrean, kendaraan yang pertama datang harus pertama keluar
(FIFO). Namun, karena ada kendala teknis, terkadang ada kendaraan di urutan
tertentu yang "mogok" dan harus dihapus dari daftar antrean secara paksa.
a. Tugas:
1. Buat struktur Node dan LinkedList.
2. Buat fungsi tambahKendaraan(plat) untuk menambah
kendaraan ke akhir list (Tail).
3. Buat fungsi hapusKendaraan(plat) untuk menghapus kendaraan
tertentu jika ia mogok di tengah antrean.

b. Logika: Melakukan traversal (penelusuran) dari head hingga menemukan
plat yang cocok, lalu menyambungkan node sebelumnya langsung ke node
sesudahnya.
'''

class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None

head = None
tail = None

def tambah_kendaraan(plat):
    global head, tail
    baru = Node(plat)
    
    if tail is None:
        head = tail = baru
    else:
        tail.next = baru
        tail = baru
    print(f"Kendaraan {plat} ditambahkan.")

def hapus_kendaraan(plat):
    global head, tail
    curr = head
    prev = None

    while curr is not None and curr.plat != plat:
        prev = curr
        curr = curr.next

    if curr is None:
        print(f"Kendaraan {plat} tidak ditemukan.")
        return

    if prev is None:
        head = curr.next
    else:
        prev.next = curr.next

    if curr == tail:
        tail = prev

    print(f"Kendaraan {plat} dihapus dari antrean.")

def tampilkan():
    curr = head
    antrean = []
    while curr:
        antrean.append(f"[{curr.plat}]")
        curr = curr.next
    print("Antrean:", " -> ".join(antrean) if antrean else "(kosong)")

# --- Uji Coba ---
tambah_kendaraan("B 1234 ABC")
tambah_kendaraan("D 8888 XYZ")
tambah_kendaraan("A 111 TUV")
tampilkan()

hapus_kendaraan("D 8888 XYZ")
tampilkan()