# 1085
x, y, w, h = map(int, input().split())

print(min(x,y,w-x,h-y))


# 3009
x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

if x[1] != x[2]:
    a = x[2]
else: a = x[0]

if y[1] != y[2]:
    b = y[2]
else: b = y[0]

print(a, b)


# 4153
while True:
    lst = list(map(int, input().split()))

    if lst == [0, 0, 0]:
        break
    else:
        lst.sort()

        if lst[2]**2 == lst[0]**2 + lst[1]**2:
            print("right")
        else:
            print("wrong")


# 2477
dens = int(input())

dir = []
size = []

for i in range(6):
    a, b = map(int, input().split())

    dir.append(a)
    size.append(b)


for i in range(6):
    if dir[i] == dir[(i+2)%6] and dir[(i+1)%6] == dir[(i+3)%6]:
        start = i
        break

area = size[(i+4)%6]*size[(i+5)%6] - size[(i+1)%6]*size[(i+2)%6]

print(area*dens)


# 1002
t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 같은 위치
    if x1==x2 and y1==y2:
        if r1==r2==0:
            print(1)
        elif r1 == r2 and r1 != 0 and r2 != 0:
            print(-1)
        else:
            print(0)
    
    else:
        dis = (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2)
        M = max(r1, r2)
        m = min(r1, r2)

        if M > dis:
            if dis + m > M:
                print(2)
            elif dis + m == M:
                print(1)
            else:
                print(0)
        
        elif M == dis:
            if m != 0:
                print(2)
            else:
                print(1)
        
        else: # M < dis
            if r1 + r2 > dis:
                print(2)
            elif r1 + r2 == dis:
                print(1)
            else: print(0)


# 1004
t = int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    lst = []
    for j in range(n):
        lst.append(list(map(int, input().split())))
    sum = 0
    for j in lst:
        dis1 = (abs(x1-j[0])**2+abs(y1-j[1])**2)**(1/2)
        dis2 = (abs(x2-j[0])**2+abs(y2-j[1])**2)**(1/2)
        
        if j[2]>dis1 and j[2]<dis2:
            sum += 1
        elif j[2]<dis1 and j[2]>dis2:
            sum += 1
    print(sum)