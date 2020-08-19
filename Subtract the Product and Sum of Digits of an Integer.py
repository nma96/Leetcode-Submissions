class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        productOfDigits = 1
        sumOfDigits = 0
        
        while n!= 0:
            temp = n%10
            n = n//10
            productOfDigits *= temp
            sumOfDigits += temp
            
        return productOfDigits - sumOfDigits