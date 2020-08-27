class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        
        for tup1, tup2 in zip(points[:-1], points[1:]):
            time +=  max(abs(tup1[0] - tup2[0]), abs(tup1[1] - tup2[1]))
        
        return time