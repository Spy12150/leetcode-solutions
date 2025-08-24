test_cases = [100, 4,200,1,3,2]
test_cases = [3,5,2,3,4,1,8,34,2,3,4,9,7,6,10,304,392]
test_cases = [2,3,5
              ]
# try unify

def longest_sequence(array):
    sol_set = set(array)
    largest_sol = 1
    for x in array:
        if x-1 not in sol_set:
            n = 1
            while x+1 in sol_set:
                x += 1
                n += 1
                print(n)
            largest_sol = max(largest_sol,n)
    return largest_sol

print(longest_sequence(test_cases))