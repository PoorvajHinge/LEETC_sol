from math import sqrt
class Solution:
    def fib(self, n: int) -> int:
        x=sqrt(5)
        y= (1/x)*((1+x)/2)**n - (1/x)*((1-x)/2)**n
        return round(y)
        
        
        