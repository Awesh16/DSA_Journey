class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)-1
        p=0
        l=0
        r=len(heights)-1
        while(l!=r):
            p=max(p,(min(heights[r],heights[l])*(r-l)))
            if(heights[r]>=heights[l]):
                l+=1
            else:
                r-=1
        return p


        
        