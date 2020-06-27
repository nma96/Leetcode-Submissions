class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        
        result = 0
        negative = False
        
        # Edge Cases
        if str[0] == '-':
            negative = True
        elif str[0] == '+':
            negative = False
        elif not str[0].isnumeric():
            return 0
        else:
            result = ord(str[0]) - ord('0')
        
        # Main conversion
        for i in range(1,len(str)):
            if str[i].isnumeric():
                result = result*10 + (ord(str[i]) - ord('0'))
                if not negative and result >= 2147483647:
                    return 2147483647
                if negative and result >= 2147483648:
                    return -2147483648
            else:
                break
        if not negative:
            return result
        else:
            return -result