# a = { 2,5,8,11,14,17,20,23,26, 29}

inputn1 = int(input('a1입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

# valueN = 0
# n = 1

# while n <= inputN:
    
#     if n == 1 :
#         valueN = inputn1
#         print(f'{n}번째 항의 값: {valueN}')
#         n += 1
#         continue
    
#     valueN += inputD
#     print(f'{n}번째 항의 값: {valueN}')
#     n += 1
    
# print(f'{inputN} 번째 항의 값: {valueN}')

# 일반항을 구하는 공식2

valueN = inputn1 + (inputN - 1) * inputD
print(f'{inputN} 번째 항의 값: {valueN}')
        