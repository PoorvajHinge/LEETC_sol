from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lis1 =[x for x in range(1,n+1)]
        perms =[p for p in permutations(lis1)]
        new_k = perms[k-1]
        return ''.join(map(str,new_k))
        
        