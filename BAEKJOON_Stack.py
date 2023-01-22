# 10828번
import sys

stack = []

n = int(sys.stdin.readline())

for i in range(0, n):
    a = sys.stdin.readline().split()

    if len(a) == 2:
        stack.append(a[1])
    
    else:
        if a[0] == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                x = stack[-1]
                stack.pop()
                print(x)
        
        elif a[0] == "size":
            print(len(stack))
        
        elif a[0] == "empty":
            if len(stack) == 0:
                print(1)
            else: print(0)
        
        elif a[0] == "top":
            if len(stack) == 0:
                print(-1)
            else: print(stack[-1])