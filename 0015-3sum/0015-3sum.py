class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            l=list()
            for i in range (0,len(nums)):
            
                if nums[i]==nums[i-1] and i>0:
                    continue
                
                big=i+1
                end=len(nums)-1
                
                while big<end:
                    sum=nums[i]+nums[big]+nums[end]
                    if(sum==0):
                        m=list()
                        m.append(nums[i])
                        m.append(nums[big])
                        m.append(nums[end])
                        while(nums[big]==nums[big+1]):
                            big+=1
                            if big==len(nums)-1:
                                break
                        while(nums[end]==nums[end-1]):
                            end-=1
                            if end==0:
                                break
                    
                        
                        
                        big+=1
                        end-=1
                        
                        l.append(m)
                    elif sum>0:
                        end=end-1
                    elif sum<0:
                        big=big+1
                
                    
            return l
                    


                    


            
        