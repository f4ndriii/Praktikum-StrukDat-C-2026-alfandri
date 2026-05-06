class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class binary_tree():
    def __init__(self):
        self.root = None

    def insert_manual(self):
        A = TreeNode('A')
        B = TreeNode('B')
        C = TreeNode('C')
        D = TreeNode('D')
        E = TreeNode('E')
        F = TreeNode('F')

        self.root = A
        A.left = B
        A.right = C
        B.left = D
        B.right = E
        C.right = F

    def traverse_pre_order(self, node):
        if node:
            print(node.data, end=' ')
            self.traverse_pre_order(node.left)
            self.traverse_pre_order(node.right)

    def traverse_inorder(self, node):
        if node:
            self.traverse_inorder(node.left)
            print(node.data, end=" ")
            self.traverse_inorder(node.right)

    def traverse_postorder(self, node):
        if node:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data, end=' ')

    def leaf_nodes(self, node, leaf_list):
        if node:
            if node.left is None and node.right is None:
                leaf_list.append(node.data)
            self.leaf_nodes(node.left, leaf_list)
            self.leaf_nodes(node.right, leaf_list)

print("SISTEM AUDIT DISTRIBUSI CEPAT SAMPAI")
print("======================================\n")
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat...\n")
print("Hasil audit:")
tree = binary_tree()
tree.insert_manual()
print(f"pre order: ",end="")
tree.traverse_pre_order(tree.root)
print(f"\nin order: ",end="")
tree.traverse_inorder(tree.root)
print(f"\npost order: ",end="")
tree.traverse_postorder(tree.root)
list_leaf = []
tree.leaf_nodes(tree.root, list_leaf)
print(f"\n\n[DATA] Gudang Ujung (Leaf Nodes): {list_leaf}")
print("\n======================================")
print("Audit Selesai!")