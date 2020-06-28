class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sLength = len(s)
        pLength = len(p)
        if sLength < pLength:
            return []
        
        pCount = collections.Counter(p)
        sCount = collections.Counter()
        res = []
        
        for i in range(sLength):
            sCount[s[i]] += 1
            if i >= pLength:
                if sCount[s[i-pLength]] == 1:
                    del sCount[s[i-pLength]]
                else:
                    sCount[s[i-pLength]] -= 1
            if pCount == sCount:
                res.append(i-pLength+1)
        
        return res
        
        # My Solution. 35/36 tests passed. Time limit exceeded
#         p_count = collections.Counter(p)
#         l = len(p)
#         res = []
        
#         for i in range(len(s)):
#             if collections.Counter(s[i:i+l]) == p_count:
#                 res.append(i)
        
#         return res