#약수

inputNumber = int(input('0보다 큰 정수입력: '))

for number in range(1, inputNumber+1):
    if inputNumber % number == 0:
        print(f'{inputNumber}의 약수: {number}')

#소수

for number in range(2, (inputNumber + 1)):
    flag = True
    for n in range(2, number):
        if number % n == 0:
            flag = False
            break
    
    if flag:
        print(f'{number}: 소수!!')
    else:
        pass
        