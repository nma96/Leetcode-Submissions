class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        
        # Put non-zeros at the start of the array
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index] = nums[i]
                index+=1
        
        # Put "Index" number of zeros at the end of the array
        for i in range(index, len(nums)):
            nums[i] = 0    
            
        