class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min1 = min(nums)
            index1 = nums.index(min1)
            nums[index1] *= multiplier
        return nums
        