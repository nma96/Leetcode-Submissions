class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Length = len(s1)
        s2Length = len(s2)
        if s1Length > s2Length:
            return False
        
        s1Count = collections.Counter(s1)
        windowCount = collections.Counter()
        
        for i, char in enumerate(s2):
            windowCount[char] += 1
            
            if i >= s1Length:
                elementFromLeft = s2[i-s1Length]
                
                if windowCount[elementFromLeft] == 1:
                    del windowCount[elementFromLeft]
                else:
                    windowCount[elementFromLeft] -= 1
            if windowCount == s1Count:
                return True
        
        return False