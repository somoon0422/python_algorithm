#일정한 공비를 가진 수열

# 다음 수열의 일반항을 구하고 n번째 항의 값과 합을 구하는 프로그램을 만들어보자.

#{2,6,18,54,162,486,1458,4374,13122,....}

'''
1. 등비수열의 일반항 : an = a1 * r^(n-1)
2. 등비수열의 합 : sn = a1 * (1 - r^n/ 1-r)
'''


inputA1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

valueN = 0
sumN = 0
n = 1
while n <= inputN:
    
    if n == 1:
        valueN = inputA1
        sumN += valueN
        print(f'{n}번째 항의 값 : {valueN}')
        print(f'{n}번째 항까지의 합 : {sumN}')
        n += 1
        continue
    
    valueN *= inputR
    sumN += valueN
    print(f'{n}번째 항의 값 : {valueN}')
    print(f'{n}번째 항까지의 합 : {sumN}')
    n += 1
    
print(f'{inputN}번째 항의 값 : {valueN}')
print(f'{inputN}번째 항까지의 합 : {sumN}')
    
    
valueN = inputA1 * (inputR ** (inputN-1)) #n번째항의 값
print(f'{inputN} 번째 항의 값 : {valueN}')

sumN = inputA1 * (1- inputR**inputN) / (1-inputR)
print(f'{inputN} 번째 항까지의 합 : {int(sumN)}')
