import math

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        positiveIndex = 0
        length = len(A)
        result = []
        
        while positiveIndex < length and A[positiveIndex] < 0:
            positiveIndex+=1
        
        negativeIndex = positiveIndex - 1
        
        while 0 <= negativeIndex and positiveIndex < length:
            if A[negativeIndex]**2 < A[positiveIndex]**2:
                result.append(A[negativeIndex]**2)
                negativeIndex -= 1
            else:
                result.append(A[positiveIndex]**2)
                positiveIndex += 1
        
        # If all positive numbers are over, insert the negative ones
        while negativeIndex >= 0:
            result.append(A[negativeIndex]**2)
            negativeIndex -= 1
        while positiveIndex < length:
            result.append(A[positiveIndex]**2)
            positiveIndex += 1
         
        return result