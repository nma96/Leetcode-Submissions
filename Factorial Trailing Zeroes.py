import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        power = 5
        
        while n//power>0:
            count += n//power
            power = power*5
        
        return count
        
#       The below method exceeds time limit
#         req = math.factorial(n)
        
#         while req%10==0:
#             count+=1
#             req=req//10
#         return count