# 수학관련함수

#합
listVar = [2,5,3.14,58,10,2]

print(f'{sum(listVar)}')

#최댓값
listVar = [2,5,3.14,58,10,2]
print(f'{min(listVar)}')

#거듭제곱
print(f'{pow(13,2)}')

#반올림
print(f'{round(3.141592, 2)}')

#math
import math

#절대값
print(math.fabs(-10))

#올림
print(f'{math.ceil(-5.21)}')

#내림
print(f'{math.floor(5.21)}')

#버림
print(f'{math.trunc(5.21)}')

#최대공약수
print(f'{math.gcd(14,21)}')

#팩토리얼
print(f'{math.factorial(10)}')

#제곱근
print(f'{math.sqrt(12)}')

import time #시간과 날짜를 관리하는 모듈

lt = time.localtime()
print(f'{lt}')

print(f'{lt.tm_year}')