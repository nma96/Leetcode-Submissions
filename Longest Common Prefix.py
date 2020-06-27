class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # https://www.youtube.com/watch?v=1YQmI7F9dJ0
        if len(strs) == 0:
            return "" 
        longestCommonPrefix = ""
        
        index = 0
        
        for character in strs[0]:
            for i in range(1, len(strs)):
                # if out of bounds with any word OR mismatch, break
                # This makes sure that sorting is not needed
                # because the loop breaks as soon as index goes bigger than the smallest word
                if index >= len(strs[i]) or character != strs[i][index]:
                    return longestCommonPrefix
            longestCommonPrefix += character
            index+=1
        return longestCommonPrefix
    
    # O(n * m) - n is number of words, m is len of smallest word