a, b, c = map(int, input().split())
sec = int(input())

c += sec
b += c // 60
a += b // 60

print(a % 24, b % 60, c % 60)
