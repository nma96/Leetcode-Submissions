class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if grid is None or len(grid)==0: return 0
        
        maxArea = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    maxArea = max(maxArea, self.dfs(grid, r, c))
        return maxArea
    
    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c]==0:
            return 0
        
        grid[r][c]=0
        
        return 1 + self.dfs(grid, r+1, c) + self.dfs(grid, r-1, c) + self.dfs(grid, r, c+1) + self.dfs(grid, r, c-1)