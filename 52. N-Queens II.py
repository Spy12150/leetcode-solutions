class Solution(object):
    def totalNQueens(self, n):
        board = ["."*n for _ in range(n)]
        col_set = set()
        diag_set1 = set()
        diag_set2 = set()
        sol = 0

        def backtrack(row):
            nonlocal sol
            if n == row:
                #arc = list(board)
                sol += 1
                return

            for x in range(n):
                col = x
                diag1 = row-x
                diag2 = row+x
                if col not in col_set and diag1 not in diag_set1 and diag2 not in diag_set2:
                    board[row] = "." * col + "Q" + "." * (n-col-1)
                    col_set.add(col)
                    diag_set1.add(diag1)
                    diag_set2.add(diag2)
                    backtrack(row+1)
                    board[row] = "."*n
                    col_set.remove(col)
                    diag_set1.remove(diag1)
                    diag_set2.remove(diag2)

        backtrack(0)
        return sol
                
# Worse original solution I did

"""class Solution(object):
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
        return results[0]"""
        

