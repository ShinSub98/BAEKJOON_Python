# 2750번
n = int(input())
lst = []
for i in range(n):
    x = int(input())
    lst.append(x)

lst.sort()

for i in lst:
    print(i)


# 2587번
lst = []
for i in range(5):
    n = int(input())
    lst.append(n)

lst.sort()

print(int(sum(lst)/5))
print(lst[2])


# 25305번
n, k = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

print(lst[n-k])


# 2751번
import sys
input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

lst.sort()

for i in lst:
    print(i)


# 10989번
import sys
input = sys.stdin.readline

n = int(input())

count = [0] * 10001

for i in range(n):
    count[int(input())] += 1

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)