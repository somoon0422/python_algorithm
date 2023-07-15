num = int(input())
c = []

for i in range(num):
    a, b = map(int, input().split())
    for i in range(b * i):
        if b * i | a * i:
            c.append(b * i | a * i)
    print(min(c))

    # 못 푼 문제
