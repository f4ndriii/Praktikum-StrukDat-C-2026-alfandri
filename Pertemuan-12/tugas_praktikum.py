class Node:
    def __init__(self, id, judul):
        self.id = id
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id, judul):
        new_node = Node(id, judul)
        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukkan: ID {new_node.id} - {new_node.judul}")
            return
        else:
            self.insert_recursive(self.root, new_node)
            print(f"[INSERT] Berhasil memasukkan: ID {new_node.id} - {new_node.judul}")

    def insert_recursive(self, current_node, new_node):
        if new_node.id < current_node.id:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_recursive(current_node.left, new_node)
        elif new_node.id > current_node.id:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.insert_recursive(current_node.right, new_node)

    def search(self, id):
        if id == self.root.id:
            print(self.root.judul)
            return
        else:
            self.search_recursive(self.root, id)

    def search_recursive(self, node, id):
        if node is None:
            print(f"[SEARCH] Mencari ID {id}... Data tidak ditemukan.")
            return
        elif id == node.id:
            print(f"[SEARCH] Mencari ID {id}... Ditemukan! Judul: {node.judul}")
            return
        elif node is not None:
            if id < node.id:
                self.search_recursive(node.left, id)
            elif id > node.id:
                self.search_recursive(node.right, id)

    def get_min(self, node=None):
        if node.left is None:
            print(f"[STATISTIK] ID Terkecil: {node.id}")
            return
        self.get_min(node.left)

    def get_max(self, node=None):
        if node.right is None:
            print(f"[STATISTIK] ID Terbesar: {node.id}")
            return
        self.get_max(node.right)

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def traversal_inorder(self, node, counter=None):
        if counter is None:
            counter = [1]

        if node is None:
            return
        self.traversal_inorder(node.left, counter)
        print(f"{counter[0]}. {node.id} - {node.judul}")
        counter[0] += 1
        self.traversal_inorder(node.right, counter)




katalog = BinarySearchTree()


# 
# 
# katalog.get_max(katalog.root)
# print(katalog.height(katalog.root))

print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=========================================")
katalog.insert(50, "Dasar Pemrograman")
katalog.insert(30, "Struktur Data")
katalog.insert(70, "Kecerdasan Buatan")
katalog.insert(20, "Matematika Diskrit")
katalog.insert(40, "Basis Data")
katalog.insert(60, "Jaringan Komputer")
katalog.insert(80, "Sistem Operasi")
print("")
print("[INFO] Koleksi Buku (In-Order Traversal):")
katalog.traversal_inorder(katalog.root)
print("")
katalog.search(60)
katalog.search(100)
print("")
katalog.get_min(katalog.root)
katalog.get_max(katalog.root)
print(f"[INFO] Tinggi (Height) Tree: {katalog.height(katalog.root)}")
print("=========================================")
print("Simulasi Selesai!")