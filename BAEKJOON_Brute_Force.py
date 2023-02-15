# 2798번
#n: 카드 숫자, m: 목표 합
n, m = map(int, input().split())

nums = list(map(int, input().split()))

result = 0

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = nums[i] + nums[j] + nums[k]
            if sum > m:
                continue
            if abs(m-result) > abs(m-sum):
                result = sum

print(result)


# 2231
n = int(input())

self = 0

for i in range(n):
    sum = i
    i = str(i)
    for j in i:
        sum += int(j)
    if sum == n:
        self = i
        break

print(self)

# 7568
n = int(input())

people = []

for i in range(n):
    people.append(list(map(int, input().split())))

rank = [1]*n

for i in range(len(people)-1):
    for j in range(i+1, len(people)):
        if people[i][0]>people[j][0] and people[i][1]>people[j][1]:
            rank[j] += 1
        if people[i][0]<people[j][0] and people[i][1]<people[j][1]:
            rank[i] += 1

for i in rank:
    print(i, end = " ")


# 1436
n = int(input())
count = 0
num = 665

while True:
    num += 1
    if str(num).count("666") != 0:
        count += 1
    
    if count == n:
        break

print(num)


# 1018
height, width = map(int, input().split())
plate = []

white = "WBWBWBWB"
black = "BWBWBWBW"

check_W = [white, black, white, black, white, black, white, black]
check_B = [black, white, black, white, black, white, black, white]

for i in range(height):
    plate.append(input())

best = 64

for h in range(height-7):
    for w in range(width-7):
        count = 0

        test = []
        test.append(plate[h][w:w+8])
        test.append(plate[h+1][w:w+8])
        test.append(plate[h+2][w:w+8])
        test.append(plate[h+3][w:w+8])
        test.append(plate[h+4][w:w+8])
        test.append(plate[h+5][w:w+8])
        test.append(plate[h+6][w:w+8])
        test.append(plate[h+7][w:w+8])

        for i in range(8):
            for j in range(8):
                if test[i][j] != check_W[i][j]:
                    count += 1
        
        if best > count:
            best = count

        count = 0

        for i in range(8):
            for j in range(8):
                if test[i][j] != check_B[i][j]:
                    count += 1
        
        if best > count:
            best = count
    

print(best)