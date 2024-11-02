class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        temp = sentence.split(" ")
        for i in range(len(temp)):
            if temp[i][0] != temp[i-1][-1]:
                return False
        return True
        