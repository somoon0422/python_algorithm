s = int(input())
total = 0
count = 0
total_list = []

for i in range(s):
    total = i + 1
    count += total
    total_list.append(i)
    if count == s:
        break
print(count)
