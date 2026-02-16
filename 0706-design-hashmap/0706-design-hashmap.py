class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:
    def __init__(self):
        # We use a prime number for the size to reduce collisions
        self.size = 1000
        self.table = [ListNode() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        cur = self.table[index]
        # Traverse the linked list at this hash index
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value  # Update existing key
                return
            cur = cur.next
        # If key not found, add new node at the end
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        cur = self.table[index].next
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        cur = self.table[index]
        # Find the node before the one we want to remove
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next  # Bypass the node to remove it
                return
            cur = cur.next