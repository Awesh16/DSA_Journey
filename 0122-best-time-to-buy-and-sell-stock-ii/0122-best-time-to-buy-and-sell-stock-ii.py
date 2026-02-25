class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=[]
        for i in range(0,len(prices)-1):
            if(prices[i]<prices[i+1]):
                l.append(prices[i+1]-prices[i])
        s=0
        for i in range(0,len(l)):
            s+=l[i]
        return s

                
            
            
        