test_score = int(input())

if 90 <= test_score <= 100:
    print("A")
elif 80 <= test_score <= 89:
    print("B")
elif 70 <= test_score <= 79:
    print("C")
elif 60 <= test_score <= 69:
    print("D")
else:
    print("F")