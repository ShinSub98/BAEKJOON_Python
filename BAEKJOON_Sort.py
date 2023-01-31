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


# 2108번
import sys
input = sys.stdin.readline

n = int(input())

count = [0] * 8001

for i in range(n):
    count[int(input()) + 4000] += 1

if count.count(max(count)) >= 2:
    firstIdx = count.index(max(count))
    idx = count.index(max(count), firstIdx+1)
else: idx = count.index(max(count))

mode = idx-4000 # 최빈값

nums = []

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            nums.append(i-4000)

print(round(sum(nums)/len(nums)))
print(nums[int(n/2)])
print(mode)
print(max(nums) - min(nums))


# 1427번
lst = list(map(int, input()))

lst.sort(reverse=True)

for i in lst:
    print(i, end="")


# 11650번
n = int(input())

nums = []

for i in range(n):
    nums.append(list(map(int, input().split())))

nums.sort(key=lambda x:x[1], reverse=False)
nums.sort(key=lambda x:x[0], reverse=False)

for i in nums:
    print(i[0], i[1])


# 1181번
n = int(input())

nums = []

for i in range(n):
    s = input()
    nums.append([s, len(s)]) # [단어, 길이]

nums.sort(key=lambda x:x[0], reverse=False)
nums.sort(key=lambda x:x[1], reverse=False)

for i in range(len(nums)-1, 0, -1):
    if nums[i] == nums[i-1]:
        del nums[i]

for i in nums:
    print(i[0])


# 10814번
n = int(input())

people = []

for i in range(n):
    info = list(map(str, input().split()))
    info[0] = int(info[0])
    people.append(info)

people.sort(key=lambda x:x [0], reverse = False)

for i in people:
    print(i[0], i[1])


# 18870번
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums2 = sorted(set(list(nums)))
dic = {nums2[i]: i for i in range(len(nums2))}

for i in nums:
    print(dic[i], end=" ")