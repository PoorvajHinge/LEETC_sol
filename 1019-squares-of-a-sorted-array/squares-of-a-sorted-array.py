class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squre = lambda x:x**2
        new_list = [squre(x) for x in nums]
        return sorted(new_list)
        