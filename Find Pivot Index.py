class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Right Sum [1, 8, 11, 17, 22, 28]
        # Left Sum [28, 27, 20, 17, 11 , 6]
        
        S = sum(nums) # Right Sum
        leftsum = 0
        
        #Left Sum
        for i, num in enumerate(nums):
            if leftsum == (S - leftsum - num):
                return i
            leftsum += num
        return -1
        