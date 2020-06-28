class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = {}
        for i in range(len(points)):
            dist[tuple(points[i])] = (points[i][0]**2+points[i][1]**2)**0.5
        
        print(dist)
        
        return heapq.nsmallest(K, dist.keys(), key=dist.get)