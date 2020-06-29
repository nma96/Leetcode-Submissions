class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    total += 4
                    
            #is 1 in 2nd row and is there any element above it, if there is, deduct 2
                    if i>0 and grid[i-1][j] == 1:
                        total -= 2
            # is 1 in 2nd coloumn and is there any element before it, if there is, deduct 2
                    if j>0 and grid[i][j-1] == 1:
                        total -= 2
        return total