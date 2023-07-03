num = []

for i in range(10):
    num.append(int(input()) % 42)
if i == 9:
    print(len(set(num)))
