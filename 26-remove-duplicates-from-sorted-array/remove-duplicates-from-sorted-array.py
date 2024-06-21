class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        se1 = set(nums)
        nums.clear()
        for i in se1:
            nums.append(i)
        nums.sort()
        return len(nums)
        