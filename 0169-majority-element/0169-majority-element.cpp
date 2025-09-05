class Solution {
public:
    int majorityElement(vector<int>& nums) {
      int count=0,el,i;
      for(i=0;i<nums.size();i++)
      {
       if(count==0)
       {
        count=1;el=nums[i];
       }
       else if(el==nums[i])
       count++;
       else 
       count--;
      }
      int ct1;
      for(i=0;i<nums.size();i++)
      {
        if(nums[i]==el)
        ct1++;
      }
      if(ct1>nums.size()/2)
      return el;
      else
      return(-1);

        }
    
};