# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp=head
        f=head.next
        e=f
        while(f is not None and f.next is not None):
            temp.next=f.next
            temp=temp.next
            f.next=temp.next
            f=f.next
        temp.next=e
        return head
        