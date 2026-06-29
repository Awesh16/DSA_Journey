class Solution:
    def reverseBits(self, n: int) -> int:
        x=0
        for i in range(32):
            if((n>>i)&1):
                x=x|(1<<31-i)
        return x