class FindNode:
    def findMiddleNode(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def findKthToLastNode(self, head, k):
        rightOfWindow = head
        leftOfWindow = head
        for i in range(k):
            rightOfWindow = rightOfWindow.next
        while rightOfWindow is not None:
            leftOfWindow = leftOfWindow.next
            rightOfWindow = rightOfWindow.next
        return leftOfWindow