# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        curr=head
        from collections import defaultdict
        x=defaultdict(int)
        while(curr!=None):
            x[curr.val]+=1
            curr=curr.next
        curr=head
        while(curr is not None and x[curr.val]>1):
            curr=curr.next
        if(curr==None):
            return None
        y=curr
        while(curr is not None):
            temp=curr.next
            while(temp is not None and x[temp.val]>1):
                temp=temp.next
            curr.next=temp
            curr=curr.next
        return y


        