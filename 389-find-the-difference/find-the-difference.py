from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = Counter(t) - Counter(s)
        add_char = list(x.keys())[0]
        return add_char
        
        