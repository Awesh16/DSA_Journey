class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a=(2**31)-1
        b=-(2**31)
        if dividend==b and divisor==-1:
            return a
        is_negative=(dividend<0)!=(divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        quotient=0
        for i in range(31,-1,-1):
            if((divisor*(2**i)<=(dividend))):
                dividend-=divisor*(2**i)
                quotient+=(2**i)
        result=-quotient if is_negative else quotient
        return max(b,min(a,result))