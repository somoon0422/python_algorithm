import math


ab = 0
while ab==0:
    a,b = map(int, input().split())

    ab += a
    ab += b


print(ab)