class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(nlogn) as heap is being constructed and accessed
        # a,b = heapq.nlargest(2, nums)
        # return (a-1)*(b-1)
        
        # O(n) - Math based solution
        first, second = 0, 0
        
        for number in nums:
            
            if number > first:
                # update first largest and second largest
                first, second = number, first
                
            else:
                # update second largest
                second = max( number, second)
        
        return (first - 1) * (second - 1)