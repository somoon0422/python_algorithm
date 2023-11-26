# floatNum = float(input('소수 입력:'))

# if floatNum - int(floatNum) >= 0.5:
#     print('올림: {}'.format(int(floatNum) + 1))
    
# else:
#     print('버림: {}'.format(int(floatNum)))

# userPoint = input()
# minAblePoint = input()

# result = '가능' if userPoint >= minAblePoint else '불가능'
# print('포인트 사용여부:{}'.format(result))

# rainPercentage = int(input('비올 확률 입력:'))

# minRainPercentage = 55

# # print('우산 챙기세요') if rainPercentage >= minRainPercentage else print('양산 챙기세요')

# if rainPercentage >= minRainPercentage:
#     print('우산챙기세요')
# else:
#     print('양산 챙기세요')

daily_temperature_range = int(input())
temperature = 11

if daily_temperature_range >= temperature:
    print('일교차:{}\n 감기조심하세요'.format(temperature +1))
else:
    print('일교차:{}\n 산책하기 좋은 날씨 입니다.'.format(temperature -2))