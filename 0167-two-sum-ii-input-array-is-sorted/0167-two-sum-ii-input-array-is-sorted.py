class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        l=list()
        for i in range(0,len(numbers)):
            diff=target-numbers[i]
            if diff in d:
                l.append(d[diff])
                l.append(i+1)
            else:
                d[numbers[i]]=i+1
        return l


        