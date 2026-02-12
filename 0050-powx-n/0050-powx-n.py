import sys

# Increase recursion depth just in case (optional, but helps with deep recursion)
sys.setrecursionlimit(2000)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1
        
        # Fix for negative numbers:
        # If n is negative, we use 1/x and make n positive
        if n < 0:
            return self.myPow(1/x, -n)

        # Your original method
        p = x * self.myPow(x, n - 1)
        return p