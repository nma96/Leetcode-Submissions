class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = collections.Counter(s)
        
        for char in t:
            if char not in sCount.keys():
                return False
            elif sCount[char] > 1:
                sCount[char] -= 1
            elif sCount[char] == 1:
                del sCount[char]
        
        if sCount is None or len(sCount) == 0:
            return True