import scores as sc

korScore = int(input('국어점수입력:'))
engScore = int(input('영어점수입력:'))
matScore = int(input('수학점수입력:'))

sc.addScore(korScore)
sc.addScore(engScore)
sc.addScore(matScore)

print(sc.getScores())
print(sc.getTotalScore())
print(sc.getAvgScore())
