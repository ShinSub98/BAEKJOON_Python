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