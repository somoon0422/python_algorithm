evenList = []; oddList = []; floatList = []

n = 1
while n < 6:
    
    try:
        num = float(input('input number: '))
    
    except:
        print('예외상황!')
        continue
    
    else:
    
        if num - int(num) != 0:
            print('float number!')
            
            floatList.append(num)
        elif num % 2 == 0:
            print('even number!')
            evenList.append(num)
            
        else:
            print('odd number!')
            oddList.append(num)
            
    n += 1

print(evenList, floatList, oddList)