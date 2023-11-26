num1= int(input('input number1: '))
num2= int(input('input number2: '))

try:
    print(f'num1 / num2: {num1 / num2}')
except Exception as e:
    print(f'exception: {e}')
    print('0으로 나눌 수 없어요')
    
print(f'num1 * num2 = {num1 * num2}')
print(f'num1 - num2 = {num1 - num2}')
print(f'num1 + num2 = {num1 + num2}')
