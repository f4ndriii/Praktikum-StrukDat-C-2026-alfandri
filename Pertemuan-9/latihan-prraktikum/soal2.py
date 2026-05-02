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
        if not self.head:
            print("List kosong...")
            return
        # Mulai dari tail/belakang
        q = self.tail
        while q:
            print(q.data)
            # Setiap perulangan mundur
            q = q.prev

    def hapus_kendaraan(self, plat):
        hapus = self.head
        while hapus:
            if hapus.data == plat:
                # Jika menghapus head
                if hapus == self.head:
                    self.head = hapus.next
                    if self.head:
                        self.head.prev = None
                    # Jika hanya ada satu elemen
                    else:
                        self.tail = None
                # Jika menghapus tail
                elif hapus == self.tail:
                    self.tail = hapus.prev
                    if self.tail:
                        self.tail.next == None
                    # Jika hanya ada satu elemen
                    else:
                        self.head = None
                        pass
                    pass
                elif hapus == self.tail:
                    self.tail = hapus.prev
                hapus.prev.next = hapus.next
                hapus.next.prev = hapus.prev
                return
            hapus = hapus.next

parkir_list = DoubleLinkedList()
parkir_list.tambah_kendaraan("B 1111 AA")
parkir_list.tambah_kendaraan("D 2222 BB")
parkir_list.tambah_kendaraan("A 3333 CC")
parkir_list.tambah_kendaraan("B 4444 DD")

print("Sebelum:")
parkir_list.tampilkan_maju()
parkir_list.hapus_kendaraan("A 3333 CC")
print("\nSesudah:")
parkir_list.tampilkan_maju()