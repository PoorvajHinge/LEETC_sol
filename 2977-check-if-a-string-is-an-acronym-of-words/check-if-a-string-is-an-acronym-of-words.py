class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        new1 = []
        for i in range(len(words)):
            new1.append(words[i][0])
        x = ''.join(new1)
        if x == s :
            return x==s
        else:
            return x==s
        