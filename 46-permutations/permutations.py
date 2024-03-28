from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        list1 = [x for x in permutations(nums)]
        return list1
        
        