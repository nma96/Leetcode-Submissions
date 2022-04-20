class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n = len(mat[0])
        for i in range(4):
            temp = [[mat[j][i] for j in range(n)] for i in range(n-1,-1,-1)]
            mat = temp
            if mat == target: 
                return True
        
        return False