import random
import sortMod2 as sm2
nums = random.sample(range(1, 1000), 100)

print(f'not sorted numbers: {nums}')

#객체 생성

sm = sm2.SortNumbers(nums)

#오름차순(ascending)
sm.setSort()
sortedNumbers = sm.getSortedNumbers()
print(f'sortedNumbers: {sortedNumbers}')

#내림차순(descending)
sm.isAscending(False)
sm.setSort()
sortedNumbers = sm.getSortedNumbers()
print(f'sortedNumbers by DESC: {sortedNumbers}')

#min & max
print(f'min: {sm.getMinNumber()}')
print(f'max : {sm.getMaxNumber()}')