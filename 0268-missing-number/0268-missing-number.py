class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=0
        y=0
        for i in range(0,len(nums)+1):
            x=x^i
        for j in range(0,len(nums)):
            y=y^nums[j]
        return x^y

        