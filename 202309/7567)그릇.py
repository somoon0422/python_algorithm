a = list(str(input()))

plus = 0

for i in range(len(a)):
    if i == 0:
        plus += 10
    elif a[i] == a[i-1]:
        plus += 5
    else:
        plus += 10

print(plus)

