class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return " "
        strs.sort()
        first=strs[0]
        last=strs[-1]
        comman=[]
        for i in range(min(len(first), len(last))):
            if(first[i]==last[i]):
                comman.append(first[i])
            else:
                break
        return "".join(comman)
        