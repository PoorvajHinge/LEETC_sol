class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_list = [''] * len(s)                #empty list with ' ' muliple baar initizle kiye 
        for char,index in zip(s,indices):
            new_list[index] = char
        return ''.join(new_list)
        
            