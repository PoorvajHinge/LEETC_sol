class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        rev = 0
        while x != 0:
            dig = x % 10
            x = x // 10
            if rev > 2147483647 // 10 or (rev == 2147483647 // 10 and dig > 7):
                return 0
            rev = rev * 10 + dig
        return -rev if is_negative else rev