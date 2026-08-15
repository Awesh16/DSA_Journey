# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        prev=head
        curr=head.next
        x=curr
        y=curr.next
        while(y is not None and y.next is not None):
            curr.next=prev
            curr=y.next 
            prev.next=curr
            prev=y
            y=y.next.next
        curr.next=prev
        prev.next=y
        return x

            
        