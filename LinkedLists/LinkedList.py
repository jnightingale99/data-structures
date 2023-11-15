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
    def add_to_head(value):
        new_node = ListNode(value)
        new_node.next = head.next
        head.next = new_node
        size += 1

    # O(n)
    def add_to_tail(value):
        new_node = ListNode(value)
        current = head
        while current != None:
            current = current.next
        current.next = new_node
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
        self.key = None
        self.value = None
        self.next = None
        self.prev = None

    def __init__(self, value):
        self.value = value

    def __init__(self, key, value):
        self.key = key
        self.value = value

def main(linked_list):
    return linked_list