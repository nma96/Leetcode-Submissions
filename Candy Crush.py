def candyCrush(board):
    m = len(board)
    n = len(board[0])

    needCrush = False

    # For Horizontal candies
    for i in range(m):
        for j in range(n - 2):
            if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) != 0:
                board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                needCrush = True

    # For Vertical candies
    for i in range(m - 2):
        for j in range(n):
            if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) != 0:
                board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                needCrush = True

    for j in range(n):
        anker_i = m - 1

        for i in range(m - 1, -1, -1):
            if board[i][j] > 0:
                board[anker_i][j] = board[i][j]
                anker_i -= 1

        for i in range(anker_i + 1):
            board[i][j] = 0

    return candyCrush(board) if needCrush else board


if __name__ == '__main__':
    board = [
        [110, 5, 112, 113, 114],
        [210, 211, 5, 213, 214],
        [310, 311, 3, 313, 314],
        [410, 411, 412, 5, 414],
        [5, 1, 512, 3, 3],
        [610, 4, 1, 613, 614],
        [710, 1, 2, 713, 714],
        [810, 1, 2, 1, 1],
        [1, 1, 2, 2, 2],
        [4, 1, 4, 4, 1014]
    ]
    print(candyCrush(board))
