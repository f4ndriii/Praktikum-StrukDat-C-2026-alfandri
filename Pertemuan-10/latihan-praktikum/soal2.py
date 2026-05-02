class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, url):
        new_node = Node(url)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.url

    def peek(self):
        if self.is_empty():
            return None
        return self.head.url

    def riwayat_size(self):
        return self.size

riwayat = Stack()
riwayat.push('youtube.com')
riwayat.push('facebook.com')
riwayat.push('instagram.com')

print("is empty:", riwayat.is_empty())
print("pop:", riwayat.pop())
print("peek:", riwayat.peek())
print("size:", riwayat.riwayat_size())