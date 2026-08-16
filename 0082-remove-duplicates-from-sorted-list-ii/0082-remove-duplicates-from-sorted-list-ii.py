class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create a dummy node pointing to the head
        dummy = ListNode(0, head)
        
        # 'prev' points to the last confirmed unique node
        prev = dummy
        
        while head:
            # If the current node has a duplicate neighbor...
            if head.next and head.val == head.next.val:
                # Move 'head' forward until we skip ALL nodes with this duplicate value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Wire 'prev.next' past all the duplicates to the node AFTER the duplicates
                prev.next = head.next
            else:
                # No duplicate detected for 'head', so 'head' is safe!
                # Advance 'prev' forward
                prev = prev.next
                
            # Move 'head' forward to continue scanning
            head = head.next
            
        return dummy.next
