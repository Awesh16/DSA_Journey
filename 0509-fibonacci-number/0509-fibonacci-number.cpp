class Solution {
public:
    int fib(int n) {
        
        int s,t=0,p=1;
        if(n==0)
        return 0;
        if(n==1)
        return 1;
        else
        {
            while(n>1)
            {s=t+p;
            t=p;
            p=s;
            n--;

            }
            return(s);
        }
    }
};