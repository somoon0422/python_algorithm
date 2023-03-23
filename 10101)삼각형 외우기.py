a = int(input())
b = int(input())
c = int(input())

if (a == b == c) and a == 60:
    print("Equilateral")
    
elif a+b+c == 180:
    if a!=b and b!=c and c!=a:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")
    


"""
# 다른 풀이
if a+b+c == 180:
    if a==b and b==c and a==c:
        print("Equilateral")
        
    elif a!=b and b!=c and c!=a:
        print("Scalene")
    
    else:
        print("Isosceles")
else:
    print("Error")
"""