inputN1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

valueN = 0
n = 1
while n <= inputN:
    
    if n == 1:
        valueN = inputN1
        print(f'{n}번째 항의 값: {valueN}')
        n += 1
        continue
    
    valueN *= inputR
    print(f'{n}번째 항의 값: {valueN}')
    n += 1
    
print(f'{inputN}번째 항의 값 : {valueN}')

# 등비수열 공식
valueN = inputN1 * (inputR ** (inputN -1))
