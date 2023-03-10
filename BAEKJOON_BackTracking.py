# 15649
n, m = map(int, input().split())

arr = [0]*m
used = [0]*(n+1)

def dfs(idx):
    if idx == m:
        print(*arr)
    else:
        for i in range(1, n+1):
            if used[i] == 0:
                used[i] = 1
                arr[idx] = i
                dfs(idx+1)
                used[i] = 0

dfs(0)


# 15650
n, m = map(int, input().split())
e = n - m

arr = [0]*m

def arrInput(start, end, idx):
    if idx == m:
        print(*arr)
        return
    for i in range(start, end):
        arr[idx] = i
        arrInput(i+1, end+1, idx+1)

arrInput(1, e+2, 0)


# 15651
n, m = map(int, input().split())

arr = [0]*m

def arrInput(idx):
    if idx == m:
        print(*arr)
        return

    for i in range(1, n+1):
        arr[idx] = i
        arrInput(idx+1)

arrInput(0)


# 15652
n, m = map(int, input().split())

arr = [0]*m

def arrInput(start, end, idx):
    if idx == m:
        print(*arr)
        return
    for i in range(start, end):
        arr[idx] = i
        arrInput(i, end, idx+1)

arrInput(1, n+1, 0)