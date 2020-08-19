class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        tempCount = 0
        for i in range(len(s)):
            
            
            if s[i] == 'R':
                tempCount +=1
            elif s[i] == 'L':
                tempCount -=1
            
            if tempCount == 0:
                count+=1 
                tempCount = 0
                
        return count