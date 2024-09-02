class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new1 = []
        for i in words:
            new1.extend(i.split(separator))
        new2 = [item for item in new1 if item]
        return new2
        