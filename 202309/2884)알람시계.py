h,m = map(int, input().split())

if m  < 45 :
    if h == 0:
        h ==23
        m += 60
    else:
        h -= 1
        m += 60
        
print(h, m-45)