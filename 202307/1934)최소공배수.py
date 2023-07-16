# 최소공배수 - LCM(Least Common Multiple)
from math import gcd

num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    print(round(a * b / gcd(a, b)))
