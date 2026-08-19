class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=0
        free=float('-inf')
        for i in intervals:
            if(free<=i[0]):
                count+=1
                free=i[1]
        return (len(intervals))-count
        