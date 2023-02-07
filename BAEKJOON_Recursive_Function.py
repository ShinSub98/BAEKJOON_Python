# 10872번
def fac(n):
    if n > 1:
        return n*fac(n-1)
    else:
        return 1

n = int(input())
print(fac(n))

# 10870번
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))


# 25501번
def recursion(s, l, r, count):
    if l >= r: return f"1 {count}"
    elif s[l] != s[r]: return f"0 {count}"
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s):
    count = 1
    return recursion(s, 0, len(s)-1, count)

t = int(input())

for i in range(t):
    s = input()
    print(isPalindrome(s))
