class Solution:
    def reverseWords(self, s: str) -> str:
        new1 = list(s.split())
        x = ' '.join(new1[::-1])
        return x
    
        