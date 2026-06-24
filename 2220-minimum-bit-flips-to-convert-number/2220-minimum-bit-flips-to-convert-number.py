class Solution:
    def minBitFlips(self, start, goal):
        m=start^goal
        count=0
        for i in range(0,32):
            if(((m)&(1<<i))):
                count+=1
        return count
