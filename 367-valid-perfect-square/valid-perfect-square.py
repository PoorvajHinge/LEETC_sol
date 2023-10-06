from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=num
        squre_root=int(sqrt(num))
        return squre_root ** 2 == x
        