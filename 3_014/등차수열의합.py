inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

vlaueN = 0
sumN = 0
n = 1

while n <= inputN:
    
    if n == 1:
        valueN = inputN1
        sumN += valueN
        print(f'{n} 번째 항까지의 합: {sumN}')
        n += 1
        continue
    
    valueN += inputD
    sumN += valueN
    print(f'{n}번째 항까지의 합: {sumN}')
    n += 1
    
print(f'{inputN}번째 항까지의 합: {sumN}')


# 등차 수열의 합을 구하는 공식

valueN = inputN1 _ (inputN-1) * inputD # n번째 항을 먼저 구한 뒤,
sumN = inputN * (inputN1 + valueN) / 2 # 1번째 항과 n번쨰 항을 더한 뒤 n을 곱하고 2로 나눈다.