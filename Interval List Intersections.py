class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        output = []
        aIndex = bIndex = 0
        
        while aIndex < len(A) and bIndex < len(B):
            intervalStart = max(A[aIndex][0], B[bIndex][0])
            intervalEnd = min(A[aIndex][1], B[bIndex][1])
            
            if intervalStart <= intervalEnd:
                output.append([intervalStart, intervalEnd])
            
            if A[aIndex][1] < B[bIndex][1]:
                aIndex += 1
            else:
                bIndex += 1
        
        return output