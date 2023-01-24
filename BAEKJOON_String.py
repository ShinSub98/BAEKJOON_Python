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
