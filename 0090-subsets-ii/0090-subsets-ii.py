class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # TRAP 1 FIX: We must sort the list first!
        # If nums = [2, 1, 2], sorting makes it [1, 2, 2].
        # This guarantees that duplicate combinations (like choosing the first 2 vs. the second 2)
        # always produce the subset in the exact same sorted order (e.g., [1, 2] instead of [2, 1]).
        nums.sort()
        
        n = len(nums)
        k = 1 << n
        
        # This master set will store our unique subsets.
        # Since set elements must be immutable, we will store them as tuples.
        l = set()
        
        for i in range(k):
            # TRAP 2 FIX: Use a normal list 'sub' to accumulate the elements.
            # Sets cannot contain other mutable sets, so 'sub' must not be a set itself.
            sub = []
            
            for j in range(n):
                if (i & (1 << j)) != 0:
                    # TRAP 3 FIX: nums[j] is just an integer (e.g., 2).
                    # We append it directly to our list. We don't call tuple() on it.
                    sub.append(nums[j])
            
            # Convert our finished 'sub' list into a tuple and add it to our master set 'l'.
            # A tuple (e.g., (1, 2)) is immutable, so Python safely allows it inside a set.
            l.add(tuple(sub))
            
        # TRAP 4 FIX: LeetCode expects List[List[int]], but our 'l' is currently a set of tuples.
        # We use a list comprehension to convert every internal tuple back to a list!
        return [list(t) for t in l]