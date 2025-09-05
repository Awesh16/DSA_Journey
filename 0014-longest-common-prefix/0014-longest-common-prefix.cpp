class Solution{	
	public:
		string longestCommonPrefix(vector<string>& str){
			int i,j,k=1,t=0,m=0; string n,l="",p="";
           
          
        
          
    for(j=0;j<str.size();j++)
    {
        if(str[j].length()<str[m].length())
        m=j;
    }
    while(k<=str[m].length())
    {
        for(i=0;i<str.size();i++)
        {
            if(str[i].substr(0,k)==str[m].substr(0,k))
            t++;
        }
        if(t==str.size())
       { l=str[m].substr(0,k);
        
        
    }k++;t=0;}

return l;
           
}

            
		}
;