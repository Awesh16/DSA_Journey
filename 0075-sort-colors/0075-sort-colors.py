class Solution:
    def sortColors(self, nums: List[int]) -> None:
        k=nums[0]
        s=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(nums[j]>=nums[i]):
                    s=nums[j]
                    nums[j]=nums[i]
                    nums[i]=s
        