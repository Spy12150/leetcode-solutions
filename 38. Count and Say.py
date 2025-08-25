def countAndSay(n):
    current_num = n%10
    digit_count = 0
    ans = 0 
    ans_digit = 0
    while n > 0:
        if n%10 != current_num:
            ans += current_num * (10**ans_digit)
            ans_digit += 1
            ans += digit_count * (10**ans_digit)
            ans_digit += 1
            current_num = n%10
            digit_count = 1
            n //= 10
            
        else: 
            digit_count += 1
            n //= 10
    ans += current_num * (10**ans_digit)
    ans_digit += 1
    ans += digit_count * (10**ans_digit)
    ans_digit += 1

    return (ans)

def series(n):
    if n>1:
        return countAndSay(n-1)        
        

