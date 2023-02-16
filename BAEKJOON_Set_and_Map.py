# 10815
n = int(input())
num_N = list(map(int, input().split()))
num_N.sort()

m = int(input())
num_M = list(map(int, input().split()))

lst = []

for i in num_M:
    left = 0
    right = n - 1
    lst.append(0)

    while left <=right:
        mid = (left+right)//2

        if num_N[mid] == i:
            lst.pop()
            lst.append(1)
            break

        elif num_N[mid] > i:
            right = mid - 1
        
        else:
            left = mid + 1

answer = " ".join(map(str, lst))
print(answer)


# 14425
n, m = map(int, input().split())

lst1 = []
lst2 = []

for i in range(n):
    lst1.append(input())
for i in range(m):
    lst2.append(input())

lst1.sort()
lst2.sort()

count = 0

for i in lst2:
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2

        if lst1[mid] == i:
            count += 1
            break
        elif lst1[mid] > i:
            right = mid - 1
        else:
            left = mid + 1

print(count)


# 1764
n, m = map(int, input().split())

strN = []
strM = []

for i in range(n):
    strN.append(input())
strN.sort()

for i in range(m):
    strM.append(input())
strM.sort()

lst = []

for i in strN:
    left = 0
    right = m-1

    while left <= right:
        mid = (left+right)//2

        if strM[mid] == i:
            lst.append(i)
            break
            
        elif strM[mid] < i:
            left = mid + 1
        
        else:
            right = mid - 1

print(len(lst))
for i in lst:
    print(i)


# 1269
n, m = map(int, input().split())

numN = list(map(int, input().split()))
numN.sort()

numM = list(map(int, input().split()))

count = n+m

for i in range(m):
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2

        if numN[mid] == numM[i]:
            count -= 2
            break

        elif numN[mid] < numM[i]:
            left = mid+1

        else:
            right = mid-1

print(count)