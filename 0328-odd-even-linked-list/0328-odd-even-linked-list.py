# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if(head is None):
            return head
        f=head.next
        k=head.next
        while(f is not None and f.next is not None):
            temp.next=f.next
            temp=temp.next
            f.next=temp.next
            f=f.next
        temp.next=k
        return head