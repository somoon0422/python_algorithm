# 수열의 일반항을 구하고 n번째 항의 값과 합을 구하는 프로그램을 만들어보자

#{4,10,16,22,28,34,40,46,52,58,64...}

'''
1. 등차수열의 일반항 : an = a1 + (n-1) * d 4*15 / 6
2. 등차수열의 합 : sn = n(a1 + an) / 2
'''

inputA1 = int(input('a1 입력: '))
inputD = int(input('공차 입력 : '))
inputN = int(input('n 입력: '))

# valueN = 0 ; sumN = 0 #n번째 항의 값과 합
# n = 1

# while n <= inputN : 
    
#     # 첫번째 항인 초기값 설정
#     if n == 1:
#         valueN = inputA1
#         sumN += valueN
#         print(f'{n}번째 항의 값: {valueN}')
#         print(f'{n}번째 항의 합: {sumN}')
#         n += 1
#         continue
    
#     valueN += inputD
#     sumN += valueN
#     print(f'{n}의 항의 값 : {valueN}')
#     print(f'{n}의 항까지의 합 : {sumN}')
#     n += 1
    
        
# print(f'{inputN}번째 항의 값: {valueN}')
# print(f'{inputN}번째 항의 합: {sumN}')


#공식을 알고있는 경우

valueN = inputA1 + (inputN - 1) * inputD
print(f'일반항: {valueN}')

sumN = inputN * (inputA1 + valueN) / 2
print(f'일반항까지의 합: {int(sumN)}')