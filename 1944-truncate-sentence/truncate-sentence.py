class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ls=list(s.split())
        newls=[]
        for i in range(0,k):
            newls.append(ls[i])
        return ' '.join(map(str,newls))
        