import sys
input = sys.stdin.readline

Q = [0]*5
for _ in range(int(input())):
    x, y = map(int,input().split())
    if x==0 or y==0:
        Q[4] += 1
        continue
    if x > 0:
        if y > 0:
            Q[0] += 1
        else:
            Q[3] += 1
    else:
        if y > 0:
            Q[1] += 1
        else:
            Q[2] += 1
print(f"Q1: {Q[0]}\nQ2: {Q[1]}\nQ3: {Q[2]}\nQ4: {Q[3]}\nAXIS: {Q[4]}")
