class ReverseList:
    def reverse_list_iteratively(self, head):
        working_pointer = head
        prev = None

        while working_pointer is not None:
            preserved_next_node = working_pointer.next
            working_pointer.next = prev
            prev = working_pointer
            working_pointer = preserved_next_node

        reversed_linked_list_head = prev
        return reversed_linked_list_head
    
    def reverse_list_recursively(self, node):
        if node is None or node.next is None:
            return node
        
        reversed_linked_list_head = reverse_list_recursively(node.next)

        node_to_my_right.next = node
        node.next = None

        return reversed_linked_list_head