class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        start = 0
        end = len(matrix)-1

        while start<end:
            mid = -((start+end)// -2)
            #print(start, end, mid, target, matrix)
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                end = mid-1
            else:
                start = mid
        if target in matrix[start]:
            return True
        return False
        