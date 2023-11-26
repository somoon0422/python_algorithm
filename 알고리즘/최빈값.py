class MaxAlgorithm:
    
    def __init__(self, ns):
        
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0
        
    def setMaxIdxAndNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0
        
        for i , n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i
    
    def getMaxNum(self):
        return self.maxNum
    
    def getMaxNumIdx(self):
        return self.maxNumIdx
    
nums = [1,3,7,6,7,7,7,12,12,17]
maxAlo = MaxAlgorithm(nums)
maxAlo.setMaxIdxAndNum()
maxNum = maxAlo.getMaxNum()
print(f'maxNum: {maxNum}')

indexes = [0 for i in range(maxNum + 1)]
print(indexes)
print(len(indexes))

for n in nums:
    indexes[n] += 1

print(indexes)

maxAlo = MaxAlgorithm(indexes)
maxAlo.setMaxIdxAndNum() #실행만 시킴
maxNum = maxAlo.getMaxNum() #출력함
maxNumIdx = maxAlo.getMaxNumIdx()
print(f'maxNum:{maxNum}')
print(f'maxNumIdx:{maxNumIdx}')
print(f'즉, {maxNumIdx}의 빈도수가 {maxNum}로 가장 높다.')
