class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        new1 = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if sorted(list(words[i])) == sorted(list(words[j])):
                    new1.append(i)
        return len(new1)
        