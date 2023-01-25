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

