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


# 2869번
import sys
input = sys.stdin.readline().rstrip

a, b, v = map(int, input().split())

up = a - b # 하루 올라갈 수 있는 높이

oneDayBefore = v - a

if oneDayBefore%up == 0:
	print((oneDayBefore//up)+1)
else: print((oneDayBefore//up)+2)

# 10250번
t = int(input())

for i in range(t):
	h, w, n = map(int, input().split())
	
	if n%h == 0:
		height = h
	else: height = n%h

	if n%h == 0:
		width = n//h
	else: width = n//h+1


	if width < 10:
		print(f"{height}0{width}")
	else: print(f"{height}{width}")


# 2839번
n = int(input())

min = n
bChanged = False

for i in range(0, n//5+2): #5키로 설탕
	for j in range(0, n//3+2): #3키로 설탕
		if 5*i + j*3 == n and min > i+j:
				min = i+j
				bChanged = True

if bChanged == False:
	print(-1)
else: print(min)

# 2775번
t = int(input())

for i in range(t):
	floor = int(input())
	ho = int(input())
	
	lst = []
	for j in range(1, ho+1):
		lst.append(j)
	
	for j in range(floor-1):
		for k in range(len(lst)-1, 0, -1):
			lst[k] = sum(lst[:k+1])
	
	print(sum(lst))