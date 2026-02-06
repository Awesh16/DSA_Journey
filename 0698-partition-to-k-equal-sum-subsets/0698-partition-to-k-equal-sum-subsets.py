class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
          # Dictionary to store (prefix_sum : frequency)
        # We initialize with {0: 1} to handle cases where the sum itself equals k
        prefix_sums = {0: 1}
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            # Check if (current_sum - k) exists in our history
            diff = current_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
            
            # Update the dictionary with the current sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        if count==k:
            return True
        else:
             return False