test_case_1 = [[3,5,2,9,2,-1,1,5,9],
          [3,5,2,9,2,-1,1,5,9],
          [3,5,2,9,2,-1,1,5,9],
          [3,5,2,9,2,-1,1,5,9],
          [3,5,2,9,2,-1,1,5,9],
          [3,5,2,9,2,-1,1,5,9],
          [3,5,2,9,2,-1,1,5,9],
          [3,5,2,9,2,-1,1,5,9],
          [3,5,2,9,2,-1,1,5,9],]

test_case_2 = [[6,-1,-1,-1,-1,-1,-1,-1,-1],
               [2,-1,-1,-1,-1,-1,-1,-1,-1],
               [5,-1,-1,-1,-1,-1,-1,-1,-1],
               [1,-1,-1,-1,-1,-1,-1,-1,-1],
               [9,-1,-1,-1,-1,-1,-1,-1,-1],
               [7,-1,-1,-1,-1,-1,-1,-1,-1],
               [8,-1,-1,-1,-1,-1,-1,-1,-1],
               [3,-1,-1,-1,-1,-1,-1,-1,-1],
               [4,-1,-1,-1,-1,-1,-1,-1,-1]]



def valid_sudoku(array1):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]

    for x in range(9):
        for y in range(9):
            v = array1[x][y]
            if v == -1: #change to if v == "." for the leetcode ver
                continue
            s = x//3 *3 + y//3
            if v in rows[x] or v in cols[y] or v in squares[s]:
                return False
            else:
                rows[x].add(v)
                cols[y].add(v)
                squares[s].add(v)
    return True
    
    
    
print(valid_sudoku(test_case_1))
print(valid_sudoku(test_case_2))
