#확률
# 조합을 구하는 방식 (nPr /R! )

def proFun():
    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))

    resultP = 1 #순열
    resultR = 1 #R 
    resultC = 1 # 조합

    for n in range(numN, (numN - numR), -1): #순열구하기
        resultP *= n
    print(resultP)

    for n in range(numR, 0, -1):
        resultR *= n
    print(resultR)

    resultC = int(resultP / resultR)
    print(resultC)
    
    return resultC

sample = proFun()
event1 = proFun()
event2 = proFun()

probability =(event1 * event2) / sample
print(f'probability : {probability * 100, 2}%')




    