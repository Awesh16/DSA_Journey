class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
      int low,high,mid,k=1;
      low=0;high=nums.size()-1;
     
      while(low<=high)
      {mid=(low+high)/2;
      if(nums[mid]==target)
     {return mid;
     k--;     }
      else if(low==high)
    break;
      else if(nums[mid]>target && high>low)
      {
        high=mid-1;
      }
      else if(nums[mid]<target && low<high)
      {
        low=mid+1;
      }
    
     }
     if(nums[mid]>target)
     return (mid);
     else
     return(mid+1);
    }
};