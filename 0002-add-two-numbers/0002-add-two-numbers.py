# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node to simplify the code
        current = dummy
        carry = 0  # To store carry-over value

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Use 0 if l1 is None
            val2 = l2.val if l2 else 0  # Use 0 if l2 is None

            total = val1 + val2 + carry
            carry = total // 10  # Carry for the next iteration
            current.next = ListNode(total % 10)  # Current digit
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next 