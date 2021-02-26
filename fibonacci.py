def nth_num(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return nth_num(n-1)+nth_num(n-2)

def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fact(n)*fact(n-1)