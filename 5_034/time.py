import time

test_path = 'C:/Users/MarkAny-N220/Desktop/sohee/zerobase/2.실습/test.txt'
lt = time.localtime()

dateStr = '[' + str(lt.tm_year) + '년' + str(lt.tm_mon) + '월' + str(lt.tm_mday) + '일] '

todaySchedule = input('오늘 일정: ')

with open(test_path, 'w', encoding='utf-8') as f:
    f.write(dateStr + todaySchedule)

with open( test_path, 'r', encoding='utf-8') as f:
    str = f.read()
    re_str = str.replace('ㅎㅎㅎ','ㅋㅋㅋ')
    print(re_str)
    
'''
'w' : 쓰기전용(파일이 있으면 덮어씌움)
'a' : 쓰기전용(파일이 있으면 덧붙임)
'x' : 쓰기전용(파일이 있으면 에러남)
'r' : 읽기전용(파일이 없으면 에러남)
'''


    