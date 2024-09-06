from math import factorial
class Solution:
    def trailingZeroes(self, n: int) -> int:
        new1 = factorial(n)
        count = 0 
        while new1%10==0 and  new1!=0:
            count+=1
            new1 = new1//10
        return count
        