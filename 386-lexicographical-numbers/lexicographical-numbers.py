class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        new_str = [str(x) for x in range(1,n+1)]
        sorted_str_numbers = sorted(new_str)
        sorted_numbers = [int(x) for x in sorted_str_numbers]
        return sorted_numbers
        