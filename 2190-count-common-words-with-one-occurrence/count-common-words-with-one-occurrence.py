from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        res = 0
        for word in count1:
            if count1[word] ==1 and count2[word] ==1:
                res+=1
        return res
        
        