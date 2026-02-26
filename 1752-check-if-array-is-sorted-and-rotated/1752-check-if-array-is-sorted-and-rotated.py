class Solution:
    def check(self, nums: List[int]) -> bool:
        k=list()
        k=nums.copy()
        nums.sort()
        l=0
        while(l<=len(nums)):
            n=list()
            n=nums[l:]+nums[:l]
            if(n==k):
                return True
            l+=1
        return False



        