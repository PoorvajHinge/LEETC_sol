class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        new_list = []
        for i in sentences:
            new_list.append(len(i.split()))
        new_list.sort(reverse =True)
        return new_list[0]
            
            
        