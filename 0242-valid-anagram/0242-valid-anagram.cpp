class Solution {
public:
    bool isAnagram(string s, string t) {
        int hash[26]={0};
            int hashh[26]={0},p=0,i;
            for(i=0;i<s.length();i++)
            {hash[s[i]-'a']++;
            }
            for(i=0;i<t.length();i++)
            {
                hashh[t[i]-'a']++;
            }
            for(i=0;i<26;i++)
            {
                if(hash[i]==hashh[i])
                {
                    p++;
                }
            }
            if(p==26)
            {
                return true;
            }
            else 
            return false;
            
    }
};