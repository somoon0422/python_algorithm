numN = int(input('numN입력: '))
numR = int(input('numR입력: '))

resultP = 1
resultR = 1
resultC = 1

for n in range(numN, (numN-numR), -1):
    print(f'n: {n}')
    resultP *= n
    
print()