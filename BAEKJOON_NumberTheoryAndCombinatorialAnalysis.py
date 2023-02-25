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