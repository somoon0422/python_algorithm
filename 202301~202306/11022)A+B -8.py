counts = int(input())

for count in range(1, counts + 1):
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(count, a, b, a + b))
