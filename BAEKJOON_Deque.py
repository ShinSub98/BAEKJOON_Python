# 10866번
import sys
input = sys.stdin.readline

a = []
front_index = 0

def pushf(a, x):
    if len(a) == front_index:
        a.append(x)
    else:
        a.append(a[-1])
        for i in range(len(a)-2, front_index, -1):
            a[i] = a[i-1]
        a[front_index] = x

def pushb(a, x):
    a.append(x)

def popf(a):
    global front_index
    if len(a) == front_index:
        return -1
    else:
        x = a[front_index]
        front_index += 1
        return x

def popb(a):
    if len(a) == front_index:
        return -1
    else:
        return a.pop()
    
def size(a):
    return len(a) - front_index

def empty(a):
    if len(a) == front_index:
        return 1
    else: return 0

def front(a):
    if len(a) == front_index:
        return -1
    else: return a[front_index]

def back(a):
    if len(a) == front_index:
        return -1
    else: return a[-1]

n = int(input())

for i in range(n):
    b = input().split()

    if b[0] == "push_front":
        pushf(a, b[1])
    
    elif b[0] == "push_back":
        pushb(a, b[1])
    
    elif b[0] == "pop_front":
        print(popf(a))
    
    elif b[0] == "pop_back":
        print(popb(a))
    
    elif b[0] == "size":
        print(size(a))
    
    elif b[0] == "empty":
        print(empty(a))
    
    elif b[0] == "front":
        print(front(a))
    
    elif b[0] == "back":
        print(back(a))