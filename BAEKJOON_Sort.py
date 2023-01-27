# 2750번
n = int(input())
lst = []
for i in range(n):
    x = int(input())
    lst.append(x)

lst.sort()

for i in lst:
    print(i)