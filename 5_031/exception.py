try:
    inputData = input('input data: ')
    numInt = int(inputData)
    
except:
    print('exception raise!!')
    print('not number!!')
    
else:
    if numInt % 2 == 0:
        print('even number!!')
    else:
        print('odd number!!')
        
finally:
    print(f'inputData: {inputData}')