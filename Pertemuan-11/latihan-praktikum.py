class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def is_empty(self):
        return self.lenght == 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.tail is None:
            self.head = self.tail = new_node
            self.lenght += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.lenght += 1

    def dequeue(self):
        if self.is_empty():
            return "Antrean kosong"
        temp = self.head
        self.head = temp.next
        self.lenght -= 1
        if self.head is None:
            self.tail = None
        return temp.nama, temp.keluhan

    def peek(self):
        if self.is_empty():
            return "Tidak ada pasien"
        return self.head.nama, self.head.keluhan

    def size(self):
        return self.lenght

    def clear(self):
        while self.head:
            self.dequeue()

    def print(self):
        temp = self.head
        count = 1
        while temp:
            print(f"{temp.nama} terdaftar dengan keluhan: {temp.keluhan} (No. antrean: {count})")
            count += 1
            temp = temp.next
        print()

antrean = QueueLinkedList()

print("="*30)
print(f"SISTEM ANTRIAN POLI UMUM\nRS Sehat Bersama")
print("="*30)

print(f"\nApakah antrean kosong? {antrean.is_empty()}")

print()
antrean.enqueue("Budi", "demam tinggi")
antrean.enqueue("Ani", "batuk pilek")
antrean.enqueue("Citra", "sakit kepala")

antrean.print()

print(f"Jumlah pasien menunggu: {antrean.lenght}")
print(f"Pasien berikutnya: {antrean.peek()}")

print("Dokter memanggil:", antrean.dequeue())

antrean.enqueue("Dodi", "nyeri perut")
print("\nDodi terdaftar dengan keluhan: nyeri perut (No. An trian: 4)\n")
print("Antrean saat ini")
antrean.print()

print("Dokter memanggil:", antrean.dequeue())
print(f"Jumlah pasien menunggu: {antrean.lenght}")

print("Sesi poliklinik selesai. Antrian dikosongkan.")
antrean.clear()
print(f"Apakah antrean kosong? {antrean.is_empty()}")