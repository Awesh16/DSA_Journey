class Solution {
public:
    int findGCD(vector<int>& nums) {
        
int n1=0,n2=10000;
for(int i=0;i<nums.size();i++)
{
n1=max(n1,nums[i]);
n2=min(n2,nums[i]);
}
int k=min(n1,n2);
int s,i;
for(i=1;i<=k;i++)
{
    if(n1%i==0 && n2%i==0)
    s=i;
}return s;
    }
};
    