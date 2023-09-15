class Solution:
    def checkRecord(self, s: str) -> bool:
        Ca=0
        Cl=0
        for i in s:
            if i=='A':
                Ca+=1
                Cl=0
            elif i=='L':
                Cl+=1
            else:
                Cl=0
            if Ca >= 2 or Cl >= 3:
                return False

        return True