import random

nums = random.sample(range(0,50), 20) #0~50 사이의 20개의 중복되지 않는 랜덤한 값 출력
print(f'nums: {nums}')

inputNum = int(input('input number: '))
print(f'inputNum : {inputNum}')

nearNum = 0
maxNum = 50

for n in nums:
    absNum = abs(n - inputNum)
    print(f'{n}의 absNum : {absNum}')
    
    if absNum < maxNum :
        maxNum = absNum
        nearNum = n
print(f'nearnum : {nearNum}')


