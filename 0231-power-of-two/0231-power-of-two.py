class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m=n%2
        if(n==1):
            return True
        if(m==0):
            n=n/2
            return(self.isPowerOfTwo(n))
        else:
            return False

        