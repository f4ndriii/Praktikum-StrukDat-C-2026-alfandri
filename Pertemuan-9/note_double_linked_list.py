class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Menambah data di akhir list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
        new_node.prev = last

    def display_forward(self):
        """Cetak dari depan ke belakang"""
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" <-> ".join(elements))

    def display_backward(self):
        """Cetak dari belakang ke depan (Membuktikan DLL bekerja)"""
        curr = self.head
        if not curr: return
        
        # Cari node terakhir dulu
        while curr.next:
            curr = curr.next
            
        # Mundur ke belakang menggunakan pointer 'prev'
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.prev
        print(" <-> ".join(elements))

# Uji Coba
dll = DoubleLinkedList()
dll.append("Node 1")
dll.append("Node 2")
dll.append("Node 3")

print("Navigasi Maju:")
dll.display_forward()

print("\nNavigasi Mundur (The Power of Prev):")
dll.display_backward()