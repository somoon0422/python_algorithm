#내가 푼 문제
n = int(input())

for _ in range(n):
    test = list(input())
    num = 0 #누적점수
    score = 0
    for j in test:
        if test[j] == 'O':
            num += 1
            score += num
        else:
            score = 0
    print(score)
    
#왜 계속 틀렸다고 하는건지 모르겠음....;;;;;;
#####################################################################
 #남이 푼 문제
    
    n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)