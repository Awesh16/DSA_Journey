class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        t=list()
        while(l<=r):
            sum=0
            n=list()
            sum=people[l]+people[r]
            if(sum<=limit):
                n.append(people[l])
                n.append(people[r])
                l+=1
                r-=1
            else:
                n.append(people[r])
                r-=1
            t.append(n)
        return len(t)
            


        
            
        