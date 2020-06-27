class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)-2):
            # if i and previour i are the same, it will result in duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # if left and left+1 is the same, it will result in duplicate
                    # so take the next occurance
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # if right and right-1 is the same, it will result in duplicate
                    # so take the next occurance (previous)
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # increment and decrement left and right after finding one pair
                    left += 1
                    right -= 1
        return result