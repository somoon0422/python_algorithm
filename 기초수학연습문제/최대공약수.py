# 100부터 1000사이의 2개의 난수에 대해서 공약수와 최대공약수를 출력하고
# 서로소 인지 출력하는 프로그램을 만들어보자
'''
1. 2개의 난수에 대해 공약수와 최대공약수를 구하기
2. 2개의 난수가 서로소 인지 확인하기
'''

import random

rNum1 = random.randint(100,1000)
rNum2 = random.randint(100,1000)

for n in range(1, min(rNum1, rNum2) + 1):
    if rNum1 % n == 0 and rNum2 % n == 0 :
        print(f'공약수 : {n}')
        maxNum = n
        
print(f'최대공약수 : {maxNum}')
if maxNum == 1:
    print(f'{rNum1} 과 {rNum2}는 서로소 이다. ')