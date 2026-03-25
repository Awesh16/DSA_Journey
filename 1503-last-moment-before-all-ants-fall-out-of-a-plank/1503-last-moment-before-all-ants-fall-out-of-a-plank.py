class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.sort(reverse=True)
        right.sort()
        if left and right:
            k=max(left[0],n-right[0])
        elif(left):
            k=left[0]
        elif(right):
            k=n-right[0]
        return k
        
            
            

            



        