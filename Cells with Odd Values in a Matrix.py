class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0 for i in range(m)] for j in range(n)]
        count = 0
        
        for index in indices:
            rIndex = index[0]
            cIndex = index[1]
            
            for i in range(m):
                matrix[rIndex][i] += 1
            
            for j in range(n):
                matrix[j][cIndex] += 1
            
        for i in range(n):
            for j in range(m):
                if matrix[i][j] %2 != 0:
                    count+=1
                    
        return count