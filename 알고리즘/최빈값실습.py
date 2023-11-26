import random
import maxScore as ms

scores = []

for i in range(100):
    rn = random.randint(71, 100)
    if rn != 100: rn -= rn % 5
    scores.append(rn)
    
print(f'scores: {scores}')
print(f'scores: {len(scores)}')

#최댓값 알고리즘
maxAlo = ms.MaxAlgorithm(scores)
maxAlo.setMaxNumIdxAndNum()
maxNum = maxAlo.getMaxNum()
print(f'maxNum: {maxNum}')

#인덱스 리스트 생성
indexes = [0 for i in range(maxNum + 1)]
print(f'indexes: {indexes}')
print(f'indexes length: {len(indexes)}')

#인덱스 리스트 빈도 저장
for n in scores:
    indexes[n] = indexes[n] + 1
print(f'indexes : {indexes}')
        
n=1
while True:
    
    maxAlo = ms.MaxAlgorithm(indexes)
    maxAlo.setMaxNumIdxAndNum()
    maxNum = maxAlo.getMaxNum
    maxNumIdx = maxAlo.getMaxNumIdx
    
    # print(f'maxNUM: {maxNum}')
    # print(f'maxNumIdx: {maxNumIdx}')
    
    if maxNum == 0:
        break
    
    print(f'{n}.{maxNumIdx}빈도수: {maxNum}\t', end='')
    print('+' * maxNum)
    
    indexes[maxNumIdx] = 0
    
    n += 1
    