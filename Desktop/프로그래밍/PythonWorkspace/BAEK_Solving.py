# 11866번
import sys
input = sys.stdin.readline

n, k = input().split()
n = int(n)
k = int(k)

queue = []
front_index = 0 # queue의 front_index
permutation = [] # 순열

for i in range(1, n+1):
    queue.append(i)

while len(permutation) != n:
    for i in range(k-1):
        queue.append(queue[front_index])
        front_index += 1
    permutation.append(queue[front_index])
    front_index += 1

print("<", end="")
for i in permutation:
    if i != permutation[-1]:
        print(f"{i}, ", end="")
    else: print(f"{i}>")