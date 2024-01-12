from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        list1 =[x for x in range(1,n+1)]
        combs = [c for c in combinations(list1,k)]
        return combs
        