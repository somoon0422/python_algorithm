person = int(input())

maxmoney = 0

for i in range(person):
    a, b, c = map(int, input().split())
    if a == b == c:
        maxmoney = max(maxmoney, 10000 + a * 1000)
    elif a == b:
        maxmoney = max(maxmoney, 1000 + a * 100)
    elif a == c:
        maxmoney = max(maxmoney, 1000 + a * 100)
    elif b == c:
        maxmoney = max(maxmoney, 1000 + b * 100)
    else:
        maxmoney = max(maxmoney, max(a, b, c) * 100)

print(maxmoney)
