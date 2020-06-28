class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = {}
        
        while n != 1:
            n = self.computeSquares(n)
        
            if n in seen:
                return False
            else:
                seen[n] = n
        
        return True   
        
    
    def computeSquares(self, n: int) -> int:
        temp = 0
        while n > 0:
            temp += (n%10)**2
            n = n//10
        return temp
    
            
            
        