class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ls1=[]
        for element in nums:
            if nums.count(element) ==1 and element not in ls1:
                ls1.append(element)
        return ls1[0]
        