class Solution(object):
    def totalNQueens(self, n):
        board = ["." *n for _ in range(n)]
        results = [0]

        def backtrack(row):
            if row == n:
                results[0] += 1
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
        return results[0]
        