# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myset=set()
        curr=head
        found=False
        while(curr!=None):
            if(curr not in myset):
                myset.add(curr)
            else:
                found=True
                p=curr
                break
            curr=curr.next
        if(found):
            return p
        else:
            return None
        