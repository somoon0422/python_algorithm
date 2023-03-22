a = int(input())
b = int(input())
c = int(input())

if a & b & c == 60:
    print("Equilateral")
elif a+b+c == 180:
    if a != b != c:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")