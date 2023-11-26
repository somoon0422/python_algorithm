import random

rNum = random.randint(100, 1000) #난수

print(f'rNum: {rNum}')

soinsuList = [] 

n = 2
while n <= rNum:
    if rNum % n == 0: #나누기 (소인수)
        print(f'소인수 : {n}')
        soinsuList.append(n)
        rNum /= n # 소인수를 자기 자신에게 다시 또 나눔 (나눠지지 않을 때 까지)
        
    else:
        n += 1 #소인수를 다 구했으니 3으로 넘어감.

print(f'soinsuList: {soinsuList}')
# 소인수에 대한 지수를 출력해보자!

tempNum = 0
for s in soinsuList:
    if tempNum != s:
        print(soinsuList.count(s)) #소인수 리스트 안에 s 가 몇 개 있는지 알려주는 함수
        tempNum = s
