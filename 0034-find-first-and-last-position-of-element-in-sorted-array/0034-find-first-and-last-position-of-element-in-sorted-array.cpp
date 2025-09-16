class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int i,j,t=0,min=-1,max=-1;vector<int>n;
        for(i=0;i<nums.size();i++)
        {if(t==0)
        {
            if(nums[i]==target)
            {
            min=i;t++;
            }
        }
        if(nums[i]==target)
        max=i;

        }n.push_back(min);
        n.push_back(max);
        return n;

        
    }
};