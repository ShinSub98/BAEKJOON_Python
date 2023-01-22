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


# 10773번
import sys
input = sys.stdin.readline

stack = []

n = int(input())

for i in range(0, n):
    money = int(input())

    if money == 0:
        stack.pop()
    else: stack.append(money)

sum = 0
for i in stack:
    sum += i

print(sum)


#9012번
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = []
    t = True # t: 성공 여부
    a = input()
    for j in a:
        if j == "(": # 좌괄호 입력
            stack.append(j)
    
        elif j == ")":# 우괄호 입력
            if len(stack) != 0:
                stack.pop()
            else: t = False
            
    
    if len(stack) == 0:
        if t == True:
            print("YES")
        else: print("NO")
    else: print("NO")


# 4949번
def str(a):
    stack = []
    for i in a:
        if i == "(" or i == "[":
            stack.append(i)
        
        elif i == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return "no"
            else: stack.pop()
        
        elif i == "]":
            if len(stack) == 0 or stack[-1] != "[":
                return "no"
            else: stack.pop()
    
    if len(stack) != 0: return "no"
    else: return "yes"
            

while True:
    a = input()
    if a == ".":
        break
    print(str(a))