class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window method
        
        #Base case
        if len(s) == 0:
            return 0
        
        maxLength = start = 0
        seen = {}
        
        for i in range(len(s)):
            # If i have seen this character
            # move start to previous index + 1
            if s[i] in seen and start <= seen[s[i]]:
                start = seen[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            seen[s[i]] = i
        
        return maxLength