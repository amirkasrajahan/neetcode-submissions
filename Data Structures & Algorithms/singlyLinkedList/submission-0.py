class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = Node()        # dummy node, real list starts at head.next
        self.tail = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head.next)
        self.head.next = node
        if not node.next:         # list was empty, new node is also the tail
            self.tail = node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        prev = self.head          # stop at the node BEFORE the one to remove
        while prev.next and index > 0:
            prev = prev.next
            index -= 1
        if not prev.next:         # index out of range
            return False
        if prev.next is self.tail:
            self.tail = prev
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        res, cur = [], self.head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res