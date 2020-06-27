class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=t1shZ8_s6jc
        rows = len(grid)
        col = len(grid[0])
        dp = [[0]*col for _ in range(rows)]
        
        dp[0][0] = grid[0][0]
        
        # Filling the 1st row
        for i in range(1,col):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        # Filling the 1st column
        for i in range(1,rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Filling the rest
        for i in range(1,rows):
            for j in range(1,col):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        print(dp)
        return dp[rows-1][col-1]
        
# Alternate, short approach
#         for i in range(1, len(grid[0])):
#             grid[0][i] += grid[0][i-1]
        
#         for i in range(1, len(grid)):
#             grid[i][0] += grid[i-1][0]
        
#         for i in range(1, len(grid)):
#             for j in range(1, len(grid[0])):
#                 grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
#         return grid[-1][-1]