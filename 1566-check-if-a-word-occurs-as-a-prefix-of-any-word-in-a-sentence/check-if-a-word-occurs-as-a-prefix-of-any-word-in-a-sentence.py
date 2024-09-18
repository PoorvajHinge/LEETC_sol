class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        new2 = []
        for i in range(0,len(words)):
            new2.append(words[i][:len(searchWord)])
        match_word  = [new2.index(word) for word in new2 if word == searchWord]
        return (match_word[0] + 1 if len(match_word) > 0 else -1)