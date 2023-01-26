# 11654번
a = input()
dType = type(a)

if dType == str:
	print(ord(a))
else: print(chr(a))


# 11720번
n = int(input())

x = input()
sum = 0
for i in x:
	sum += int(i)

print(sum)


# 10809번
alphabet = "abcdefghijklmnopqrstuvwxyz"

s = input()

for i in alphabet:
	check = False

	for j in range(len(s)):
		if s[j] == i:
			check = True
			x = j
			break
	
	if check == True:
		print(x, end=" ")
	else: print(-1, end= " ")


# 2675번
n = int(input())

for i in range(n):
	x = input().split()
	x[0] = int(x[0])
	for j in x[1]:
		for k in range(x[0]):
			print(j,end="")
	if i != n-1:
		print("")


# 1152번
s = input().split(sep = " ")

front = 0

for i in s:
	if i == "":
		front+=1

print(len(s) - front)


# 2908번
x, y = input().split()

n = int(x[2]+x[1]+x[0])
m = int(y[2]+y[1]+y[0])

if n>m:
	print(n)
else: print(m)


# 5622번
s = input()

sum = 0

for i in s:
	if i == 'A' or i == 'B' or i == 'C': sum += 3

	elif i == 'D' or i == 'E' or i == 'F': sum += 4

	elif i == 'G' or i == 'H' or i == 'I': sum += 5

	elif i == 'J' or i == 'K' or i == 'L': sum += 6

	elif i == 'M' or i == 'N' or i == 'O': sum += 7

	elif i == 'P' or i == 'Q' or i == 'R' or i == 'S': sum += 8

	elif i == 'T' or i == 'U' or i == 'V': sum += 9

	elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z': sum += 10

	else: sum+= 11

print(sum)

# 1157번
import sys
input = sys.stdin.readline().rstrip

str = input().upper()

alphabet = [] # 단어 속 알파벳
counts = [] # 알파벳 개수

for i in str:
	alphabet.append(i)

alphabet = list(set(alphabet))

for i in alphabet:
	counts.append(str.count(i))

if len(counts) >= 2:
	# 같은 수가 두개 있을 때
	if sorted(counts)[-1] == sorted(counts)[-2]:
		print("?")

	else:
		print(alphabet[counts.index(max(counts))])

else:
	print(alphabet[0])