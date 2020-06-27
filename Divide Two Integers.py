class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Bad test case -2147483648/-1 == 2147483648
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        res = 0
        multiplier = 1
        div = abs(dividend)
        divr = abs(divisor)
        
        if div < divr:
            return 0
        
        # Find max multiplier
        while div >= (divr << 1):
            divr = divr << 1
            multiplier = multiplier << 1
        
        # Reduce multiplier checking if valid
        while multiplier >= 1 and div > 0:
            if div - divr >= 0:
                div -= divr
                res += multiplier
            divr = divr >> 1
            multiplier = multiplier >> 1
            
        
        # Negative
        if bool(dividend < 0) ^ bool(divisor < 0):
            return 0-res
        return res