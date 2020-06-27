class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) if s.split() else 0 # One line code
        
#         count = 0
        
#         for index,let in enumerate(s[::-1]):
#             if index==0 and let == ' ':
#                 continue
#             elif let!=' ':
#                 count+=1
#             elif let==' ':
#                 break
#         return count