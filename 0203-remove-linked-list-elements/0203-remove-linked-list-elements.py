# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy_head = ListNode(-1)
        # dummy_head.next = head
        
        # current_node = dummy_head
        # while current_node.next != None:
        #     if current_node.next.val == val:
        #         current_node.next = current_node.next.next
        #     else:
        #         current_node = current_node.next
                
        # return dummy_head.next
        t=ListNode()
        t.next=head
        temp=t
        while temp.next != None:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
               temp=temp.next
        return t.next
