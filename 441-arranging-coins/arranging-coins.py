class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        while(n>0):
            n-=i
            i+=1
            if(n<i):
                break
        return (i-1)
                
                
        