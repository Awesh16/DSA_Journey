class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        l=list()
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if(diff in d.keys()):
                l.append(d[diff])
                l.append(i)
            d[nums[i]]=i
        return l

        