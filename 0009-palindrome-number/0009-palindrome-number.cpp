class Solution {
public:
    bool isPalindrome(int x) {
    long n=x,s=0,m,j;
    if(n<0)
    return false;
    while(n!=0)
    {
        m=n%10;
        s=(s*10)+m;
        n=n/10;
    }
    if(s==x)
    return true ;
    else return false;
    }
};