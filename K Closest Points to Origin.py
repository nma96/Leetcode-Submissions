class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for x,y in points:
            minHeap.append([(x**2+y**2)**0.5, x, y])
            
        heapq.heapify(minHeap)
        result = []
        
        while k != 0: 
            distance, x, y = heapq.heappop(minHeap)
            result.append([x,y])
            k -= 1
            
        return result
            