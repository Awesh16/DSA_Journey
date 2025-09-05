class Solution {
public:
    int majorityElement(vector<int>& nums) {
       unordered_map<int,int>hash;
        int i,k=0,l;
        for(i=0;i<nums.size();i++)
        {
            hash[nums[i]]++;
        }
        for(i=0;i<nums.size();i++)
        {if(hash[nums[i]]>k)
        {
            k=hash[nums[i]];
            l=i;
        }}
        return nums[l];

        }
    
};