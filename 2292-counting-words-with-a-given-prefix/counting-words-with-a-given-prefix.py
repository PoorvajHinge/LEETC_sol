class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        new2 = []
        for i in range(0,len(words)):
            new2.append((words[i][:len(pref)]))
        match_word  = [word for word in new2 if word == pref]
        return len(match_word)
        