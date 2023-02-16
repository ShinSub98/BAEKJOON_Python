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