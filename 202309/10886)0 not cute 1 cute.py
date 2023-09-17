n = int(input())
y,h = 0,0

for i in range(n):
    vote = int(input())
    if vote == 1 :
        y += 1
    else:
        h += 1
        
if y > h :
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
    