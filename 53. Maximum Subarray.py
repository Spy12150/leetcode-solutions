test_case_1 = [1,2,1,2,3]
test_case_1_k = 3
test_case_2 = [5,2,2,5,8,9,2,3,4,2,2]
test_case_2_k = 4

def sliding_window(array,k):
    first = 0
    container = []
    largest_sum = 0
    
    for right in range(len(array)):
        while array[right] in container:
            container.pop(0)
        container += [array[right]]

        
        if len(container) == k:
            largest_sum = max(largest_sum,sum(container))
        container.pop()

    return(largest_sum)
    
print(sliding_window(test_case_1,test_case_1_k))
print(sliding_window(test_case_2,test_case_2_k))