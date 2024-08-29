class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new1 = sorted(list(zip(heights,names)) ,reverse=True)
        char_set = [name for name , name in new1]
        return char_set