class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if J is "" or len(J)==0: return 0
        
        jCount = collections.Counter(J)
        count = 0
        
        for i in S:
            if jCount[i]>=1:
                count += jCount[i]
        
        return count