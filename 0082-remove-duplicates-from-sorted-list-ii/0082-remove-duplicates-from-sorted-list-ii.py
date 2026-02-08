# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        prev,cur=dummy,head
        while cur:
            if cur.next and cur.next.val==cur.val:
                while cur.next and cur.next.val==cur.val:
                    cur=cur.next
                prev.next=cur.next
            else:
                prev=prev.next
            cur=cur.next
        return dummy.next