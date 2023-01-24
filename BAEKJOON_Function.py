# 4673번
nums = []

for i in range(10000):
	nums.append(0)

def selfNumber(x):
	n = x
	for i in str(x):
		n += int(i)
	return n

for i in range(1, 10001):
	a = selfNumber(i)
	if 1 <= a <= 10000:
		nums[a-1] = 1

for i in range(10000):
	if nums[i] == 0:
		print(i+1)


# 1065번
nums = []

def check100(x):
	if int(str(x)[1]) - int(str(x)[0]) ==  int(str(x)[2]) - int(str(x)[1]):
		return True


n = int(input())
count = 0

for i in range(1, n+1):
	if i < 100:
		count += 1
	
	elif 100 <= i < 1000:
		if check100(i) == True:
			count += 1

print(count)