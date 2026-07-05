class Solution(object):
    def solveNQueens(self, n):
        board = ["." *n for _ in range(n)]
        results = []

        def backtrack(row):
            if row == n:
                arc = list(board)
                results.append(arc)
                return

            for x in range(n):
                if is_valid(row, x):
                    board[row] = "." * x + "Q" + "." * (n-x-1)
                    backtrack(row+1)
                    board[row] = "." * n
        
        def is_valid(row, col):
            for y in range(row):
                if board[y][col] == "Q":
                    return False
                if row-y <=col and board[y][col-(row-y)] == "Q":
                    return False
                if col+(row-y)< n and board[y][col+(row-y)] == "Q":
                    return False
            return True

        backtrack(0)
        return results