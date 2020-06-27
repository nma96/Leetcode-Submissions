class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = 0
        
        for i in range(0,len(digits)):
            output += digits[i]*(10**(len(digits)-i-1))
            
        output+=1
        return list(str(output))
                
        