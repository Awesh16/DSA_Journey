class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        sum=0
        t=len(nums)
        n=len(nums)
        while(r<n):
            sum=sum+nums[r]
            while(sum>=target):
                t=min(t,r-l+1)
                sum-=nums[l]
                l+=1
            r+=1
        if(l==0 and sum < target):
            return 0
        return t
            

            


        