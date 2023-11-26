nums = []

n=1
while n < 6:
    
    try:
        num = int(input('input number: '))
    
    except:
        print('예외발생!')
        continue
    
    else:
        if num % 2 == 0:
            nums.append(num)
            n += 1
        
        else:
            print('홀수 입니다.', end='')
            print('다시 입력하세요.')
            continue
    
print(nums)
        
        