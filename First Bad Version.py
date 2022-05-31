# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        res = 1
        while left <= right: 
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid-1
                res = mid
            else: 
                left = mid + 1
            
        return res