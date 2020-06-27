class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >=0:
                sum += int(a[i])
                i-=1
            if j >=0:
                sum += int(b[j])
                j-=1
            result = str(sum%2) + result
            carry = sum//2
            
        if carry > 0:
            result = "1" + result
        
        return result