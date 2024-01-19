class BSTNode:
    def __init__(self, data):
        self.data = data # data is an integer number
        self.left = None # duplicate goes left (always)
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def contains_at(self, node: BSTNode, data) -> bool:
        if not node:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self.contains_at(node.left, data)
        else:
            return self.contains_at(node.right, data)

    def contains(self, data) -> bool:
        return self.contains_at(self.root, data)

    def count_at(self, node) -> int:
        if not node:
            return 0
        return 1 + self.count_at(node.left) + self.count_at(node.right)

    def count(self) -> int:
        return self.count_at(self.root)

    def insert_to(self, node: BSTNode, data):
        if data <= node.data:
            if node.left:
                self.insert_to(node.left, data)
            else:
                node.left = BSTNode(data)
        else:
            if node.right:
                self.insert_to(node.right, data)
            else:
                node.right = BSTNode(data)

    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self.insert_to(self.root, data)