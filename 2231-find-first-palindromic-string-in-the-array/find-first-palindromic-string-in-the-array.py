class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        new1 = [x for x in words if x ==x[::-1]]
        return new1[0] if new1 else ""
        