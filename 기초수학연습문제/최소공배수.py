# 100부터 1000사이의 2개의 난수에 대해서 최대공약수와 최소공배수을 알아보는 프로그램을 만들자

import random

rNum1 = random.randint(100, 1000)
rNum2 = random.randint(100, 1000)

print(f'rNum1 : {rNum1}')
print(f'rNum2 : {rNum2}')

maxNum = 0

for n in range(1 , min(rNum1, rNum2) + 1):
    if rNum1 % n == 0 and rNum2 % n == 0 :
        print(f'공약수 : {n}')
        maxNum = n
        
print(f'최대공약수 : {maxNum}')

minNum = (rNum1 * rNum2) // maxNum
print(f'최소공배수: {minNum}')

