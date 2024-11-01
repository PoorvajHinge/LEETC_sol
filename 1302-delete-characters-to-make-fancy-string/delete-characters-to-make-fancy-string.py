class Solution:
    def makeFancyString(self, s: str) -> str:
        new_final = []
        for i in range(len(s)):
            if len(new_final) >=2 and new_final[-1]==s[i] and new_final[-2]==s[i]:
                continue
            new_final.append(s[i])
        return ''.join(new_final)
        