class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.size = 0

    # O(n)
    def get(index):
        current = head.next
        for i in range(index):
            current = current.next
        return current.value

    # O(1)
    def addToHead(value):
        newNode = ListNode(value)
        newNode.Next = head.Next
        head.Next = newNode
        size += 1

    # O(n)
    def addToTail(value):
        newNode = ListNode(value)
        current = head
        while current != None:
            current = current.Next
        current.Next = newNode
        size += 1

    # O(n)
    def add_at_index(value, index):
        new_node = ListNode(value)
        current = head
        for i in range(index):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        size += 1

    def delete_at_index(index):
        current = head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        size -= 1

class ListNode:
    def __init__(self):
        self.Key = None
        self.Value = None
        self.Next = None
        self.Prev = None

    def __init__(self, value):
        self.Value = value

    def __init__(self, key, value):
        self.Key = key
        self.Value = value

def Main(linkedList):
    return linkedList