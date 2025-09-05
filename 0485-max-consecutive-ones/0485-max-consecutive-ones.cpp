class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int i,j=0,n=0;
        for(i=0;i<nums.size();i++)
        {
            if(nums[i]==1)
            {
                n++;
                j=max(j,n);
            }
            else
            n=0;

            }
        
        return j;}
    }
;