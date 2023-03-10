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