class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return self.helper(s, i+1, j) or self.helper(s, i, j-1)
            i += 1
            j -= 1
                
        return True
    
    def helper(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True