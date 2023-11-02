class PrintList:
    def printListIterative(self, head):
        workingPointer = head

        while workingPointer is not None:
            print(workingPointer.value)
            workingPointer = workingPointer.Next
    
    def printListRecursive(self, node):
        if node is None:
            return
        print(node.Value)
        printListRecursive(node.Value)

    def reverse_print_list_iterative(head):
        stack = []
        working_pointer = head
        while working_pointer is not None:
            stack.append(working_pointer)
            working_pointer = working_pointer.next
        while len(stack) != 0:
            print(stack[-1].value)
            stack.pop()

    def reversePrintListRecursive(node):
        if node is not None:
            return
        reversePrintListRecursive(node.Next)
        print(node.Value)
