class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=list()
        d=defaultdict(int)
        for i in range(0,len(nums)):
            d[nums[i]]+=1
            if(d[nums[i]]>len(nums)/3):
                l.append(nums[i])
        return list(set(l))
        
        
        