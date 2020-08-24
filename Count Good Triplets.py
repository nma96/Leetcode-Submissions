class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        
        for num1 in range(len(arr)-2):
            for num2 in range(num1+1, len(arr)-1):
                if abs(arr[num1] - arr[num2]) <= a:
                    for num3 in range(num2+1, len(arr)):
                        if (abs(arr[num2] - arr[num3]) <= b) and (abs(arr[num3] - arr[num1]) <= c):
                            count+=1
        
        return count
    
        