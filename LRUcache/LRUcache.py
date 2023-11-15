from LinkedLists.LinkedList import ListNode
from Hashtables.hashtable import Hashtable

class LRUcache:
    def __init__(self, maxCapacity):
        self.hashtable = Hashtable()
        self.head = ListNode()
        self.tail = ListNode()
        self.max_capacity = None
        self.total_items_in_cache = 0

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
    
    # look up in hashtable to get node and move node to head
    def get(key):
        node = hashtable.get(key)

        if node is None:
            return null
        
        move_to_head(node)

        return node.value
    
    # look up hashtable to get node
    # if it exists then update node in list
    # if it doesn't create a new node
    # if we're at capacity then add to front and add to hashtable, remove last node from list and hashtable, increase count by 1
    # if we're under capacity then add to front ad add to hashtable 
    def put(key, value):
        node = hashtable.get(key)

        if node == null:
            new_node = ListNode(value)
            add_to_head(newNode)
            hashtable.Put(key, newNode)
            total_items_in_cache += 1

            if max_capacity > total_items_in_cache:
                removed_node = remove_from_list(tail.prev)
                hashtable.remove(removed_node.key, removed_node.value)
                total_items_in_cache -= 1

        node.value = value
        move_to_head(node)

    def add_to_head(node):
        node.prev = head
        node.next = head.next
        head.next = node
        head.next.prev = node

    def remove_from_list(node):
        saved_next = node.next
        saved_prev = node.prev

        saved_next.prev = saved_prev
        saved_prev.next = saved_prev.next

        return node
    
    def move_to_head(node):
        remove_from_list(node)
        add_to_head(node)