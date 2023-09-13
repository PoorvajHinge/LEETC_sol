class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if(x==x[::-1]):
            return x==x[::-1]
        else:
            return x==x[::-1]
        