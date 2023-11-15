class FindNode:
    def find_middle_node(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def find_kth_to_last_node(self, head, k):
        right_of_window = head
        left_of_window = head
        for i in range(k):
            right_of_window = right_of_window.next
        while right_of_window is not None:
            left_of_window = left_of_window.next
            right_of_window = right_of_window.next
        return left_of_window