class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        n=len(s)
        h=set()
        ma=0
        while(r<n):
            while(s[r] in h):
                h.remove(s[l])
                l+=1
            h.add(s[r])
            ma=max(ma,r-l+1)
            r+=1
        return ma

            
        
        