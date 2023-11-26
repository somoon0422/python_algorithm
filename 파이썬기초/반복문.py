limitweight = 2200
currentweight = 800
date = 1

while True:
    if currentweight >= 2200:
        break
    
    date += 1
    currentweight += 70

print('이유식 중단 날짜: {}일'.format(date))

import reverseStr

