class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, url):
        self.stack.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

riwayat = Stack()

riwayat.push('facebook.com')
riwayat.push('youtube.com')
riwayat.push('instagram.com')

print("stack:", riwayat.stack)
print("pop:", riwayat.pop())
print("peek:", riwayat.peek())
print("size:", riwayat.size())