class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedS = "".join(c for c in s if c.isalnum()).lower()
        
        left, right = 0, len(cleanedS)-1
        
        while left<right: 
            if cleanedS[left] != cleanedS[right]:
                return False
            left, right = left+1, right-1
        
        return True
            