class Solution:
    def countSeniors(self, details: List[str]) -> int:
        new1 = [detail[11:13] for detail in details if int(detail[11:13])>60]
        return len(new1)
        
        
        