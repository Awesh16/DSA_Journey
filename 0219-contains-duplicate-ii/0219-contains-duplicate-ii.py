class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Dictionary to store {value: last_seen_index}
        index_map = {}
        
        for i, num in enumerate(nums):
            # Check if we've seen this number before
            if num in index_map:
                # Check if the gap is small enough
                if i - index_map[num] <= k:
                    return True
            
            # Update the dictionary with the latest index
            index_map[num] = i
            
        return False