import sys

n = int(sys.stdin.readline())

count = 1
max = 1
a = 1
if n == 1:
	print("1/1")
else:
	check = True
	while check == True:
		turn += 1
		count += 1
		a = turn
		while a != 1:
			count += 1
			a -= 1
			if count == n:
				check = False
				break
	b = turn - a + 1
	print(f"{a}/{b}")
		





