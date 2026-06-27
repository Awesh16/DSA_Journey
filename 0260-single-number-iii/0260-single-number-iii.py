class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        g1=0
        g2=0
        for i in nums:
            x=x^i
        k=x & (-x)
        for i in nums:
            if((k & i)==0):
                g1=g1^i
            else:
                g2=g2^i
        if(g1>g2):
            return [g2,g1]
        else:
            return [g1,g2]
        