class MinAlgorithm:
    
    def __init__(self, ns):
        
        self.nums = ns
        self.minNum = 0
        
    def getMinNum(self):
        self.getMinNum = self.nums[0]
        
        for n in self.nums:
            if self.minNum > n:
                self.minNum = n
        
        return self.minNum
    
nums = [-2,4,5,7,10,0,8,20,-100]
ma = MinAlgorithm(nums)
minNum = ma.getMinNum()
print(minNum)
