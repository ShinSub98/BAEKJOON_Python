def fibo(x):
    global countFibo
    if x == 1 or x == 2:
        return 1
    else:
        countFibo += 1
        return fibo(x-1)+fibo(x-2)

def fibo_dp(x, lst):
    global countFibo_dp
    if x == 1 or x == 2:
        return lst[x]
    else:
        for i in range(3, x+1):
            countFibo_dp += 1
            lst[i] = lst[i-1] + lst[i-2]
        return lst[i]
    
countFibo = 0
countFibo_dp = 0

fibo_lst = [0]*50
fibo_lst[1], fibo_lst[2] = 1, 1

n = int(input())

fibo(n)
fibo_dp(n, fibo_lst)

print(countFibo, countFibo_dp)