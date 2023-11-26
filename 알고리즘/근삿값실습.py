import near

scores = []

kor = int(input('input kor score: '))
scores.append(kor)

eng = int(input('input eng score: '))
scores.append(eng)

mat = int(input('input mat score: '))
scores.append(mat)

sci = int(input('input sci score: '))
scores.append(sci)

his = int(input('input his score: '))
scores.append(his)

totalScore = sum(scores)
print(f'totalscore : {totalScore}')

avgScore = totalScore / len(scores)
print(f'avgScore : {avgScore}')


grade = near.getNearNum(avgScore)
print(f'grade: {grade}')