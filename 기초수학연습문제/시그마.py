# 첫째날 쌀 두톨을 받고 둘째 날부터는 하루 전의 2배에 해당하는 쌀을 받는다고 할 때,
# 30일째 되는 날 받게되는 쌀의 개수를 수열과 시그마로 나타내고 이를 출력하는 프로그램을 만들자.


# { 2,4,8,16,32,64,128,256,512,1024,...}

inputA1 = int(input('a1 입력 : '))
inputR = int(input('공비 입력 : '))
inputN = int(input('n 입력: '))

valueN = 0 ; sumN = 0

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
    
print(f'{inputN} 번째 항의 값: {valueN}')
print(f'{inputN} 번째 항까지의 합 : {format(sumN, ",")}')


# an = a1 * r^(n-1)
valueN = inputA1 * inputR ** (inputN - 1)
# sn = a1 * (1- r^n) / 1-r
sumN = inputA1 * (1- (inputR ** inputN)) / (1 - inputR)

print(valueN)
print(sumN)