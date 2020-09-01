class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Better Implementation:
        assert(self.backtrack(board, 0, 0))
        return
                    
    def backtrack(self, board: List[List[str]], r: int, c: int) -> bool:
        # Go to next empty space
        while board[r][c] != '.':
            c += 1
            if c == 9: c, r = 0, r+1
            if r == 9: return True
        # Try all options, backtracking if not work
        for k in range(1, 10):
            if self.isValidSudokuMove(board, r, c, str(k)):
                board[r][c] = str(k)
                if self.backtrack(board, r, c):
                    return True
        board[r][c] = '.'
        return False
    
    def isValidSudokuMove(self, board: List[List[str]], r: int, c: int, cand: int) -> bool:
        # Check row
        if any(board[r][j] == cand for j in range(9)): return False
        # Check col
        if any(board[i][c] == cand for i in range(9)): return False
        # Check block
        br, bc = 3*(r//3), 3*(c//3)
        if any(board[i][j] == cand for i in range(br, br+3) for j in range(bc, bc+3)): return False
        return True
        
        # My implementation
#         def possible(y, x, n):
#             # Check the row
#             for i in range(0, 9):
#                 if board[y][i] != '.' and int(board[y][i]) == n:
#                     return False
            
#             # Check the column
#             for j in range(0, 9):
#                 if board[j][x] != '.' and int(board[j][x]) == n:
#                     return False
            
#             # Check the box
#             x0 = (x//3)*3
#             y0 = (y//3)*3
            
#             for i in range(0, 3):
#                 for j in range(0, 3):
#                     if board[y0 + i][x0 + j] != '.' and int(board[y0 + i][x0 + j]) == n:
#                         return False
#             return True
        
#         for y in range(9):
#             for x in range(9):
#                 if board[y][x] == '.':
#                     for n in range(1, 10):
#                         if possible(y, x, n):
#                             board[y][x] = str(n)
#                             if self.solveSudoku(board):
#                                 return True
#                             board[y][x] = '.'
#                     return False
#         return True
        
        