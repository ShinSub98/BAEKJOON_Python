n = int(input())
submultiples = sorted(list(map(int, input().split())))

print(submultiples[0]*submultiples[-1])