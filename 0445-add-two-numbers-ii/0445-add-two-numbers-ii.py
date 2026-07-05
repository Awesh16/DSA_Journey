# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(l1):
    prev=None
    temp=l1
    while temp is not None:
        front=temp.next
        temp.next=prev
        prev=temp
        temp=front
    return prev
       
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1=l1
        r2=l2
        d1=0
        d2=0
        while r1 is not None:
            d1=(d1*10)+r1.val
            r1=r1.next
        while(r2 is not None):
            d2=(d2*10)+r2.val
            r2=r2.next
        d3=d1+d2
        dummy=ListNode(d3%10)
        curr=dummy
        d3=d3//10
        while(d3!=0):
            curr.next=ListNode(d3%10)
            d3=d3//10
            curr=curr.next
        return reverse(dummy)
        