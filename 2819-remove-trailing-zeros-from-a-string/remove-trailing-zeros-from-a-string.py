class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num=str(num)
        while(num[-1]=='0'):
            num=num[:-1]
        return num
        
        
        
        