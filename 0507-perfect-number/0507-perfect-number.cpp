class Solution {
public:
    bool checkPerfectNumber(int num) {
        if(num<=0)
        return false;
        int i,s=0;
        for(i=1;i<=num/2;i++)
        {
            if(num%i==0)
            s=s+i;
        }if(s==num)
        return true;
        else 
        return false;
    }
};