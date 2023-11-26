def calculator(n1, n2):
    return n1+n2

returnValue = calculator(10,20)
print(f'returnValue: {returnValue}')


calculator = lambda n1,n2 : n1+n2
returnValue = calculator(10,20)
print(f'returnValue: {returnValue}')