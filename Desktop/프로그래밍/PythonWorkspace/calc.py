num = int(input("자연수를 입력 "))

#  약수
def submultiple(n):
    if n<=0:
        return print('자연수를 입력해주세요.')
    else:
        global submuls
        submuls = []
        for i in range (1, n+1):
            if n%i == 0:
                submuls.append(i)
    return print("{}의 약수:".format(n),*submuls)
submultiple(num)


# ~까지의 배수
max_mul = int(input("몇 까지 배수를 구할까? "))

def multiple(n, m): # n은 최초값, m은 배수의 최대 값
    if n <= 0 or m <=0 or n>m:
        return print("잘못된 입력")
    else:
        global muls
        muls = []
        for i in range (1, int((m/n)+1)):
            muls.append(n*i)
    return print("{}까지의 배수:".format(max_mul),*muls)
multiple(num, max_mul)


# 공약수
num2 = int(input("공약수를 구할 수 "))

def common_divisors(n, m):
    if n <= 0 or m <=0:
        return print("잘못된 입력")
    else:
        global codis
        codis = []
        if n <= m:
            for i in range (1, n+1):
                if n%i == 0 and m%i == 0:
                    codis.append(i)
        else:
            for i in range (1, m+1):
                if n%i == 0 and m%i == 0:
                    codis.append(i)
    return print("{0}과 {1}의 공약수:".format(n, m),*codis)
common_divisors(num, num2)


# 공배수
num3 = int(input("어느 수와의 공배수를 구할까? "))
max_comuls = int(input("몇 까지의 공배수를 구할까? "))

def common_multiple(n, m, x): # n, m은 공배수를 구할 수 / x는 최대 값
    if n <= 0 or m <=0 or x <= n or x<= m:
        return print("잘못된 입력")
    else:
        global nmuls, mmuls, comuls # nmul는 n의 배수, mmuls는 m의 배수, comuls는 공배수
        nmuls, mmuls, comuls = [], [], []
        for i in range (1, int((x/n)+1)): # x까지의 n의 배수
            nmuls.append(n*i) 
        for i in range (1, int((x/m)+1)): # x까지의 m의 배수
            mmuls.append(m*i) 
        for i in range (0, len(nmuls)): # n과 m의 배수들이 담긴 리스트들을 각각 비교하여 comuls에 추가
            for t in range (0, len(mmuls)):
                if nmuls[i] == mmuls[t]:
                    comuls.append(mmuls[t])
    return print("{0}와 {1}의 공배수는".format(num, num3), *comuls)
                     
common_multiple(num, num3, max_comuls)