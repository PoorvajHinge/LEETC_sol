class Solution:
    def compressedString(self, word: str) -> str:
        char = word[0]
        count = 1
        comp = []
        for c in word[1:]:
            if c == char and count < 9:
                count += 1
            else:
                comp += [str(count), char]
                char = c
                count = 1
        comp += [str(count), char]
        return "".join(comp)
        