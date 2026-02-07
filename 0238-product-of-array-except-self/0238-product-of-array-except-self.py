class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        k=nums.copy()
        k=1
        p=0
        t=[]
        for i in range (0,len(nums)):
            if(nums[i]==0):
                p+=1
                t.append(i)
                continue
            k*=nums[i]
        if(p>1):
            k=0
        
        if(p!=0):
            for i in range(0,len(nums)):
                if i in t:
                    l.append(k)
                else:
                    l.append(0)
        else:
            for i in range(0,len(nums)):
                l.append(int(k/nums[i]))
        return l
            

        