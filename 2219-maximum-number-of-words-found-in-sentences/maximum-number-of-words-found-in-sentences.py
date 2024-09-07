class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        new1 = []
        for i in range(len(sentences)):
            new1.append(len(sentences[i].split()))
        return max(new1)
            