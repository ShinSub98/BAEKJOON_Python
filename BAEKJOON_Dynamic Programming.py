# 24416
def fibo(x, lst):
    if x == 1 or x == 2:
        return 1
    lst[1], lst[2] = 1, 1
    for i in range(3, n+1):
        lst[i] = lst[i-1]+lst[i-2]
    return lst[x]

n = int(input())
lst = [0]*41

print(fibo(n, lst), n-2)
