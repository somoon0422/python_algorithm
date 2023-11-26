class NotUseZeroException(Exception):
    
    def __init__(self, n):
        super().__init__(f'{n}은(는) 사용할 수 없습니다.')
    
    
def divCarculator(n1, n2):
    
    if n2 == 0:
        raise NotUseZeroException(n2)
    
    else:
        print(f'{n1} / {n2} = {n1/ n2}')
        
num1 = int(input('input number1: '))
num2 = int(input('input number2: '))

try:
    divCarculator(num1, num2)
except NotUseZeroException as e:
    print(e)