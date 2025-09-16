class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int i,j=0,k=0;
       sort(nums.begin(),nums.end());
       for(i=0;i<nums.size()-1;i++)
       {
        if(nums[i+1]-nums[i]==0)
        {
          continue;
        }
        else if(nums[i+1]-nums[i]==1)
       j++;
        else{
            if(j>k)
            k=j;
            j=0;
        }
        
       }
       if(j>k)
       k=j;
       return (k+1);
    
    }
};