
def reverse(x):
    y = x
    if x <0:
        x = abs(x)
    x = int(str(x)[::-1])
    if y<0:
        return -x
    return x

print(reverse(-123))
    
            
        