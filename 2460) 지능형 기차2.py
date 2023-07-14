result = 0
num = 0

for _ in range(10):
    a, b = map(int, input().split())  # 내린사람 #탄사람
    num -= a
    num += b
    result = max(result, num)
print(result)
