evenList = []; oddList = []; floatList = []; dataList = []

n = 1
while n < 6:
    
    try:
        data = input('input number: ')
        floatNum = float(data)
    except:
        print('exception raise!!')
        print('not number!!')
        continue
    else:
        if floatNum - int(floatNum) != 0:
            print('float number!!')
            floatList.append(floatNum)
        else:
            if floatNum % 2 == 0:
                print('even number!!')
                evenList.append(floatNum)
            else:
                print('odd number!!')
                oddList.append(floatNum)
        n += 1
    finally:
        dataList.append(data)
        
print(f'evenList: {evenList}')
print(f'oddList: {oddList}')
print(f'floatList: {floatList}')
print(f'dataList: {dataList}')