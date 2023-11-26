nums =[]

n = 1
while n < 6:
    try:
        num = int(input('input number: '))
    except:
        print('숫자가 아닙니다.')
        continue #while 문이 계속 진해됨.
    
    nums.append(num)
    n += 1
    
        

print(f'nums: {nums}')