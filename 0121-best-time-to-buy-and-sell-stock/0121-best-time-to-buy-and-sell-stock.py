class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=0
        k=100000
        diff=0
        for i in range(0,len(prices)):
            if prices[i]<k and i!=len(prices)-1:
                k=prices[i]
                n=0
            if prices[i]>n and i!=0:
                n=prices[i]
                dif=n-k
                if diff<dif:
                    diff=dif 
                 
            
        
        return diff
        
        
        
        
