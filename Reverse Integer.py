class Solution:
    def reverse(self, x: int) -> int:
        # Simple case
        if x >= -9 and x <= 9:
            return x
        
        negative = False
        
        if x < 0:
            negative = True
            x *= -1
        else:
            negative = False
        
        result = 0
        
        for i in range(len(str(x))):
            result = result*10 + x%10
            x = x//10
            if result >= 2147483647:
                return 0
        
        if not negative:
            return result
        else:
            return -result