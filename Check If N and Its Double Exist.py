class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for val in arr:
            if val * 2 in seen:
                return True
            if val % 2 == 0:
                if val / 2 in seen:
                    return True
            seen.add(val)
        return False