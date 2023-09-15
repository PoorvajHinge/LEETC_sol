class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y=s.split()
        z=y[-1]
        return len(z)
        