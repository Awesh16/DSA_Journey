class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        k=1<<n
        l=[]
        for i in range(0,k):
            sub=[]
            for j in range(0,n):
                if(i&(1<<j)):
                    sub.append(nums[j])
            l.append(sub)
        return l
            

        