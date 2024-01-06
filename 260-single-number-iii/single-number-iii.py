class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        unique_elements = [x for x in nums if nums.count(x) == 1]
        return unique_elements
        