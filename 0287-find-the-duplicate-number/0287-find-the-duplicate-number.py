class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums) - 1
        duplicate = 0
        
        # Scan each of the 32 bit positions
        for bit in range(32):
            mask = 1 << bit
            actual_count = 0
            expected_count = 0
            
            # Count set bits in the array and the range [1, n]
            for i in range(len(nums)):
                # Actual count from the array
                if (nums[i] & mask) != 0:
                    actual_count += 1
                # Expected count from range [1, n] (skip index 0)
                if i > 0 and (i & mask) != 0:
                    expected_count += 1
            
            # If we have more 1s than expected, this bit belongs to our duplicate!
            if actual_count > expected_count:
                duplicate |= mask
                
        return duplicate