class MaxAlgorithm:
    
    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        
    
    def getMaxNum(self):
        
        self.maxNum = self.nums[0]
        
        for n in self.nums:
            if self.maxNum < n :
                self.maxNum = n
                
        return self.maxNum

ma = MaxAlgorithm([-2,-4,5,7,10,0,8,20,-11])
maxNum = ma.getMaxNum()
print(f'maxNum: {maxNum}')
