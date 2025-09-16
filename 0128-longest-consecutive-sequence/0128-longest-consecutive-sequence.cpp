class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int i,j=0,k=0;
      int p=nums.size();
      int largest =0;
      unordered_set<int>st;
      for(i=0;i<p;i++)
      st.insert(nums[i]);
      for(auto it:st)
    {
        if(st.find(it-1)==st.end())
        {
            int cnt=1;
            int x=it;
            while(st.find(x+1)!=st.end())
            { 
                cnt++;
                x++;
            }
            largest=max(largest,cnt);
        }
    }
    return largest;
    }
};