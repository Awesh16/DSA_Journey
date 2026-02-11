class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base Case: Anything to the power of 0 is 1
        if n == 0:
            return 1
        
        # Handling Negative Power: x^-n is the same as (1/x)^n
        if n < 0:
            x = 1 / x
            n = -n
        
        # Recursive Step (Divide and Conquer)
        # We calculate the result for half the power (n // 2)
        half = self.myPow(x, n // 2)
        
        # If n is even: x^n = x^(n/2) * x^(n/2)
        if n % 2 == 0:
            return half * half
        
        # If n is odd: x^n = x * x^(n/2) * x^(n/2)
        # We need that extra 'x' because integer division discarded it
        else:
            return x * half * half