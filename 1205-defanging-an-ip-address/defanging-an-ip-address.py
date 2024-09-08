class Solution:
    def defangIPaddr(self, address: str) -> str:
        new1 = []
        for i in address:
            if i == '.':
                new1.append("[.]")
            else:
                new1.append(i)
        return ''.join(new1)