class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        new2 = []
        for i in range(len(words)):
            if x in words[i]:
                new2.append(i)
        return new2