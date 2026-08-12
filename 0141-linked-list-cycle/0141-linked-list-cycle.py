# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        p1=head
        p2=head
        yes=False
        while(p2!=None and p2.next!=None):
            p1=p1.next
            p2=p2.next.next
            if(p1==p2):
                yes=True
                break
        if(yes):
            return True
        else:
            return False

        