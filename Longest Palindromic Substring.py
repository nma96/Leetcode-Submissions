class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ""
        
        start = end = 0
        
        for i in range(len(s)):
            len1 = self.expandFromCentre(s, i, i)
            len2 = self.expandFromCentre(s, i, i+1)
            length = max(len1, len2)
            if length > end-start:
                start = i - (length - 1) // 2
                end = i + length // 2
            
        return s[start:end+1]
    
    def expandFromCentre(self, s, left, right):
        l,r = left, right
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        
        return r-l-1