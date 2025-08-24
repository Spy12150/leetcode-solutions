test_case = [1,2,3,4,5]

"""def two_pass(array):
    left_array = [1]*len(array)
    right_array = [1]*len(array)
    left_track = 1
    right_track = 1
    sol_array = [1]*len(array)
    for i in range(len(array)):
        left_array[i] *= left_track
        left_track *= array[i]
    for i in range(len(array)):
        right_array[len(array)-i] *= right_track
        right_track *= array[len(array)-i]
    for i in range(len(sol_array)):
        sol_array[i] = left_array[i]*right_array[i]
    return sol_array"""

def two_pass_2(array):
    n = len(array)
    left = [1] *(n+1)
    right= [1] *(n+1)
    for i in range(1,n+1,1):
        left[i]=left[i-1]*array[i-1]
    for i in range (n-1,-1,-1):

        right[i] = right[i+1] *array[i]
    res = [-1] *n
    for i in range(n):
        res[i] = left[i]*right[i+1]
    print(left,right)

    return res

print(two_pass_2(test_case))
        