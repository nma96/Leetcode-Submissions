class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Create a window
        pointer1 = 0
        pointer2 = len(needle)
        if needle == '':
            return 0
        
        # In a for loop, until you find needle, slide the window
        for i in range(len(haystack)):
            substring = haystack[pointer1:pointer2]
            if substring == needle:
                return pointer1
            pointer1+=1
            pointer2+=1
        return -1
                
                