class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        k=1<<n
        l=set()
        for i in range(0,k):
            sub=[]
            for j in range(0,n):
                if(i&(1<<j)):
                    sub.append(nums[j])
            l.add(tuple(sub))
        return [list(t) for t in l]
            

        