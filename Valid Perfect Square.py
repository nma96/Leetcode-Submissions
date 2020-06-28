class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return (num**0.5)//1 == (num**0.5) # Simple solution but uses sqrt in a way
        
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        
        return False