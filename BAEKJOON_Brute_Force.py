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