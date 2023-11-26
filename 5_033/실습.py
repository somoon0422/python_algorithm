class PasswordLengthShortException(Exception):
    
    def __init__(self, str):
        super().__init__(f'{str}: 길이 5미만')
        
class PasswordLengthLongException(Exception):
    
    def __init__(self, str):
        super().__init__(f'{str}: 길이 10초과')
        
class PasswordhWrongException(Exception):
    
    def __init__(self, str):
        super().__init__(f'{str}: 잘못된 비밀번호')
        

password = input('input admin password: ')

try:
    if len(password) < 5:
        raise PasswordLengthShortException(password)
    elif len(password) > 10:
        raise PasswordLengthLongException(password)
    elif password != 'password':
        raise PasswordhWrongException(password)
    elif password == 'password':
        print('빙고!')
    
except PasswordLengthShortException as e1:
    print(e1)

except PasswordLengthLongException as e2:
    print(e2)
    
except PasswordhWrongException as e3:
    print(e3)

    
    
    
