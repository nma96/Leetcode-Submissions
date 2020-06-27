class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        
        while left < right:
            temp = self.waterContent(height[left], height[right], (right-left))
            maxWater = max(maxWater, temp)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater
    
    def waterContent(self, len1, len2, width):
        return min(len1, len2) * width