class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        new_count = s.count('1')
        new_S = [x for x in s]
        final = [x for x in s if x!='1']
        if new_count == 1:
            final.append('1')
        elif(new_count>1):
            final.append('1')
            for i in range(new_count -1):
                final.insert(0,'1')
        return ''.join(final)