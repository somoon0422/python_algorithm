import random
import sortMod3 as sm
import copy

scores = random.sample(range(50, 101), 20)

print(f'scores: {scores}')
print(f'scores: {len(scores)}')


result = sm.sortNumber(copy.deepcopy(scores))
print(f'scores: {scores}')
print(f'result : {result}')


result = sm.sortNumber(copy.deepcopy(scores), asc=False)
print(f'scores: {scores}')
print(f'result: {result}')