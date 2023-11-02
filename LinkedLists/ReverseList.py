class ReverseList:
    def reverseListIteratively(self, head):
        workingPointer = head
        prev = None

        while workingPointer is not None:
            preservedNextNode = workingPointer.Next
            workingPointer.Next = prev
            prev = workingPointer
            workingPointer = preservedNextNode

        reversedLinkedListHead = prev
        return reversedLinkedListHead
    
    def reverseListRecursively(self, node):
        if node is None or node.Next is None:
            return node
        
        reversedLinkedListHead = reverseListRecursively(node.Next)

        nodeToMyRight = node.Next
        nodeToMyRight.Next = node
        node.Next = None

        return reversedLinkedListHead