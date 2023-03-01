n = int(input())
submultiples = sorted(list(map(int, input().split())))

print(submultiples[0]*submultiples[-1])

# 2609
def gcd(n, m):
    while m>0:
        n, m = m, n%m
    return n

a, b = map(int, input().split())

print(gcd(a,b))
print(a*b//gcd(a,b))

# 1943
def gcd(n, m):
    while m>0:
        n, m = m, n%m
    return n

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a*b//gcd(a,b))


# 3036
n = int(input())

rings = list(map(int, input().split()))

x = rings[0]

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

for i in range(1, len(rings)):
    g = gcd(x,rings[i])
    print(f"{x//g}/{rings[i]//g}")


# 1010
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = 1
    b = 1
    for j in range(n):
        a *= m
        m -= 1
    
    for j in range(1, n+1):
        b *= j

    print(int(a/b))


# 9375
t = int(input())

for i in range(t):
    n = int(input())
    dic = {}
    for j in range(n):
        a, b = input().split()
        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 2
    sum = 1
    lst = list(dic.values())
    for j in lst:
        sum *= j
    
    print(sum-1)


# 1676
n = int(input())

fac = 1

for i in range(1, n+1):
    fac *= i

fac = str(fac)
sum = 0
for i in range(len(fac)-1, -1, -1):
    if fac[i] == '0':
        sum += 1
    else:
        break

print(sum)


# 11050
a, b = map(int, input().split())

sum1 = 1
sum2 = 1

for i in range(b):
    sum1 *= a
    a -= 1

for i in range(1, b+1):
    sum2 *= i

print(sum1//sum2)


# 11051
a, b = map(int, input().split())

sum1 = 1
sum2 = 1

for i in range(b):
    sum1 *= a
    a -= 1

for i in range(1, b+1):
    sum2 *= i

answer = sum1//sum2

print(answer%10007)