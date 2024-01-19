class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.count = 0

    def append_to(self, node: ListNode, data):
        if not node:
            return ListNode(data)
        else:
            node.next = self.append_to(node.next, data)
        return node

    def append(self, data):
        self.first = self.append_to(self.first, data)
        self.count +=1

    def length_from(self, node: ListNode) -> int:
        if not node.next:
            return 1
        return self.length_from(node.next) + 1

    def length(self) -> int:
        return self.count

    def nth_from(self, node: ListNode, n: int):
        if n == 0:
            return node.data
        return self.nth_from(node.next, n - 1)

    def nth(self, n: int):
        if n < 0 or n >= self.length():
            raise IndexError("Bad linked list index")
        # 0 <= n < self.length()
        return self.nth_from(self.first, n)
    def remove_from(self, node: ListNode, data_to_remove):
        if not node:
            raise Exception
        if node.data == data_to_remove:
            self.count -=1
            return node.next
        node.next = self.remove_from(node.next, data_to_remove)
        return node
    def remove(self, n:int):
        self.first = self.remove_from(self.first, n)
