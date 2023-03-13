# 13241
a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

def gcd(a,b):
    while a*b != 0:
        a, b = b%a, a
    return b

print((a*b)//gcd(a,b))


# 1735
n1, n2 = map(int, input().split())
m1, m2 = map(int, input().split())

def gcd(a,b):
    while a*b != 0:
        a, b = b%a, a
    return b

def lcm(a,b):
    return (a*b)//gcd(a, b)

num2 = lcm(n2, m2)

n1 *= num2//n2
m1 *= num2//m2
num1 = n1+m1

if gcd(num1, num2) != 1:
    while gcd(num1, num2) != 1:
        num1, num2 = num1//gcd(num1, num2), num2//gcd(num1, num2)

print(num1, num2)


# 17103
primes = []
arr = [False, False] + [True]*999999

for i in range(2, len(arr)):
    if arr[i]:
        primes.append(i)
    for j in range(2*i, len(arr), i):
        arr[j] = False

t = int(input())

for q in range(t):
    n = int(input())
    count = 0
    for i in primes:
        if i >= n:
            break
        if arr[n-i] and i <= n-i:
            count+=1

    print(count)


# 4134
def check(x):
    for i in range(3, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

t = int(input())

for q in range(t):
    n = int(input())
    if n <= 2:
        print(2)
        continue

    while True:
        if check(n):
            print(n)
            break
        elif not check(n):
            n += 1