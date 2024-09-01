from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new1 = Counter(nums)
        new2 = [x for x , count in new1.items() if count>len(nums)//2]
        return new2[0]