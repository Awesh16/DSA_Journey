class Solution {
public:
    bool checkPerfectNumber(int num) {
        if(num<=1)
        return false;
        int i,s=1;
        for(i=2;i<=sqrt(num);i++)
        {
            if(num%i==0)
            s=s+i+(num/i);
        }if(s==num)
        return true;
        else 
        return false;
    }
};