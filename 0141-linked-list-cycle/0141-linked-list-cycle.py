# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        from collections import defaultdict
        d=defaultdict(int)
        curr=head
        yes=False
        while(curr!=None):
            d[curr]+=1
            if(d[curr]>1):
                yes=True
                break
            curr=curr.next
        if(yes):
            return True
        else:
            return False
        