class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        new1 = [x for x in word]
        new2 = []
        for i in patterns:
            if i in word:
                new2.append(i)
        return len(new2)