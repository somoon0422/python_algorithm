def sendSMS(msg):
    
    if len(msg) > 10:
        raise Exception('길이 초과! MMS 전환 후 발송!!', 1)
    
    else:
        print('sms발송!')
        

def sendMMS(msg):
    
    if len(msg) <= 10:
        raise Exception('길이 미달!! SMS전환 후 발송!!', 2)
    
    else:
        print('MMS발송!!')

msg = input('input message: ')

try:
    sendMMS(msg)
except Exception as e:
    print(f'e: {e.args[0]}')
    print(f'e: {e.args[1]}')
    
    if e.args[1] == 1:
        sendMMS(msg)
    elif e.args[1] == 2:
        sendSMS(msg)