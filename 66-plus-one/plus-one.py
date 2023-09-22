class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=0
        for i in digits:
            res=res*10+i
        final=(res+1)
        final=str(final)
        lst=[]
        for i in final:
            lst.append(int(i))
        return lst

        