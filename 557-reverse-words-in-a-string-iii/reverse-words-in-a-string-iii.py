class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        final=[]
        for i in x:
            final.append(i[::-1])
        return ' '.join(map(str,final))
        