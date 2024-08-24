from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count1 = Counter(arr)
        row1  = [x for x , count in count1.items() if count == 1]
        if len(row1)>=k:
            return row1[k-1]
        else:
            return ""