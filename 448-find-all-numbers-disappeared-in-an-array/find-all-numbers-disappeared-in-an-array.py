class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = set(range(1,len(nums)+1))  ##[1,2,3,4,5,6,7,8]
        nums_set = set(nums)   ##yahape [1,2,3,4,7,8] rahega
        new1 = (all_nums - nums_set)   ##sare numbers all_nums me jo hai vo rahgee but excluding nums_set vale hat jaegee 
        return new1
        