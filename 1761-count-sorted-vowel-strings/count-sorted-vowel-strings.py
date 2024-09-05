from math import comb
class Solution:
    def countVowelStrings(self, n: int) -> int:
        k = 5
        return comb(n + k - 1, k - 1)