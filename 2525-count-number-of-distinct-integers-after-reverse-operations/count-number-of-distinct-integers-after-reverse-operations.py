class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new_list=[str(x)[::-1] for x in nums]
        new_int_list = [int(x) for x in new_list]
        final_list = nums + new_int_list
        return (len(set(final_list)))
        