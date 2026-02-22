class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base Case
        if n == 0:
            return 1
        
        # 1. Handle Negative Numbers
        # If n is negative, flip x to 1/x and make n positive
        if n < 0:
            return self.myPow(1/x, -n)
        
        # 2. Divide and Conquer
        # Calculate the result for half of n
        half = self.myPow(x, n // 2)
        
        # 3. Combine the results
        if n % 2 == 0:
            # If n is even: x^10 = x^5 * x^5
            return half * half
        else:
            # If n is odd: x^11 = x * (x^5 * x^5)
            # The extra 'x' accounts for the remainder we lost in integer division
            return x * half * half