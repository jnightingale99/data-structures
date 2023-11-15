class PrintList:
    def print_list_iterative(self, head):
        working_pointer = head

        while working_pointer is not None:
            print(working_pointer.value)
            working_pointer = working_pointer.next
    
    def print_list_recursive(self, node):
        if node is None:
            return
        print(node.value)
        print_list_recursive(node.value)

    def reverse_print_list_iterative(head):
        stack = []
        working_pointer = head
        while working_pointer is not None:
            stack.append(working_pointer)
            working_pointer = working_pointer.next
        while len(stack) != 0:
            print(stack[-1].value)
            stack.pop()

    def reverse_print_list_recursive(node):
        if node is not None:
            return
        reverse_print_list_recursive(node.next)
        print(node.value)
