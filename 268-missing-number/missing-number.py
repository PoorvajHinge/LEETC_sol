class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lst1=[]
        for i in range(len(nums)+1):
            lst1.append(i)
        uncommon_elements = list(set(nums).symmetric_difference(set(lst1)))
        return uncommon_elements[0]
        