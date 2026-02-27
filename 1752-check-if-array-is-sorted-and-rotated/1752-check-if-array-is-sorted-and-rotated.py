class Solution:
    def check(self, nums: List[int]) -> bool:
        k=0
        for i in range(0,len(nums)):
            if(nums[i]>nums[(i+1)%len(nums)]):
                k+=1
        return k<=1
        
            