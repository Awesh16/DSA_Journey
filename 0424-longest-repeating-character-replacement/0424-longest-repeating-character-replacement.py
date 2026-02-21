class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=defaultdict(int)
        l=0
        r=0
        max_f=0
        n=len(s)
        ans=0
        while(r<n):
            d[s[r]]+=1
            max_f=max(max_f,d[s[r]])
            while((r-l+1)-max_f>k):
                d[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)   
            r+=1
        return ans
        
    
