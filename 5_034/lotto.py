import random

uri = './lotto.txt'

def writeNumbers(nums):
    for idx, num in enumerate(nums):
        with open(uri, 'a') as f:
            if idx < len(nums) - 2:
                f.write(str(num) + ', ')
            elif idx == len(nums) -2:
                f.write(str(num))
            elif idx == len(nums) -1:
                f.write('\n')
                f.write('bonus: '+ str(num))
                f.write('\n')
                
rnums = random.sample(range(1, 46), 7)
#print(f'rnums : {rnums}')

writeNumbers(rnums)