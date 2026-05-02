class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_petugas(self, nama):
        baru = Node(nama)
        if not self.head:
            baru.next = baru
            self.head = baru
            self.tail = baru

        else:
            self.tail.next = baru
            self.tail = baru
            self.tail.next = self.head

    def giliran_berikutnya(self, n):
        if not self.head:
            print("Belum ada petugas...")
            return
        else:
            giliran = self.head
            for i in range(n):
                print(f"Giliran {i+1}: {giliran.data}")
                giliran = giliran.next

list = CircularLinkedList()

list.tambah_petugas("Andi")
list.tambah_petugas("Budi")
list.tambah_petugas("Citra")
list.tambah_petugas("Dewi")
list.giliran_berikutnya(6)
