class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        new_list_neg = [x for x in nums if x<0]
        new_list_pos = [x for x in nums if x>0]
        count_neg = len(new_list_neg)
        count_pos = len(new_list_pos)
        return max(count_neg,count_pos)
        