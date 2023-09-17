a = input()
b = input()

result = 0
index = 0

while len(a) - index >= len(b):
    if a[index:index+len(b)] == b:
        result += 1
        index += len(b)
    else:
        index += 1
        
print(result)