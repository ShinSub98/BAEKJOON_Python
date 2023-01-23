num=int(input())

## 1번. 교차 대입
a, b=1,1
print(a,b, end=" ")
for i in range (3, num+1):
	c=a+b
	print(c, end=" ")
	if i%2 == 0:
		a=c
	else:
		b=c
print(" ")

## 2번. 밀어내기
d,e=1,1
print(d,e, end=" ")
for i in range (2, num):
	c=d+e
	print(c, end=" ")
	d=e
	e=c
print(" ")

## 3번. list.append
list = [1,1]
for i in range(2, num):
	list.append(list[i-2]+list[i-1])
print(*list)

## 4번. 재귀함수
def fibo(n):
	if n<=2: return 1
	else: return fibo(n-1) + fibo(n-2)

for i in range (1, num+1):
	print(fibo(i), end=" ")
print(" ")