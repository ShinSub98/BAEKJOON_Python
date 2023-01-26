# 1712번
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

s = c-b


if b>=c:
	print(-1)
else:
	sale = a//s
	print(sale+1)


# 2292번
import sys
input = sys.stdin.readline

a = int(input())

x=1
count = 1

while a>x:
	x += count*6
	count +=1

print(count)


# 1193번
import sys
input = sys.stdin.readline().rstrip

x = int(input()) # 순서

n = 1
sum = 1

while sum < x:
	n += 1
	sum += n

sum -= n	
x -= sum
a = n+1-x

if n%2==1: # 홀수줄이면
	print(f"{a}/{x}")
else:
	print(f"{x}/{a}")