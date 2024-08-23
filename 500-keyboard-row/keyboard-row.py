class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for i in words:
            low = set(i.lower())
            if low <= row1 or low <= row2 or low <= row3:
                result.append(i)
        
        return result
