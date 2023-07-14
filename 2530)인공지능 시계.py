a, b, c = map(int, input().split())
sec = int(input())

b += sec // 60
c += sec % 60

if b == 60:
    a += 1
elif c == 60:
    b += 1
elif a == 24:
    a, b, c == 0

print(a, b, c)
