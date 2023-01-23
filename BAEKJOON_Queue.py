# 18258번
import sys
input = sys.stdin.readline

queue = []
front_index = 0

n = int(input())

def push(x):
    queue.append(x)

def pop():
    global front_index # 함수 내에서 값을 수정하기 위해선 전역변수로 선언!
    if len(queue) != front_index:
        x = queue[front_index]
        front_index += 1
        return x
    else: return -1

def size():
    return len(queue) - front_index

def empty():
    if len(queue) == front_index:
        return 1
    else: return 0

def front():
    if len(queue) != front_index:
        return queue[front_index]
    else: return -1

def back():
    if len(queue) != front_index:
        return queue[-1]
    else: return -1

for i in range(n):
    str = input().split()

    if len(str) == 2:
        push(str[1])
    
    elif str[0] == "pop":
        print(pop())
    
    elif str[0] == "size":
        print(size())
    
    elif str[0] == "empty":
        print(empty())
    
    elif str[0] == "front":
        print(front())

    elif str[0] == "back":
        print(back())


# 2164번
import sys
input = sys.stdin.readline

n = int(input())
card = []
front_index = 0

for i in range(n):
    card.append(i+1)

if len(card) == 1:
    print(card[0])


else:
    while True:
        front_index += 2
        card.append(card[front_index-1])
        if len(card) - front_index == 1:
            break

    print(card[front_index])


# 11866번
import sys
input = sys.stdin.readline

n, k = input().split()
n = int(n)
k = int(k)

queue = []
front_index = 0 # queue의 front_index
permutation = [] # 순열

for i in range(1, n+1):
    queue.append(i)

while len(permutation) != n:
    for i in range(k-1):
        queue.append(queue[front_index])
        front_index += 1
    permutation.append(queue[front_index])
    front_index += 1

print("<", end="")
for i in permutation:
    if i != permutation[-1]:
        print(f"{i}, ", end="")
    else: print(f"{i}>")