from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [p for p in permutations(nums)]
        return set(perms)