import sys
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(1000000) 
        num1 = ''.join(map(str,num))
        res = int(num1) + k
        new1 = [int(x) for x in str(res)]
        return new1
        