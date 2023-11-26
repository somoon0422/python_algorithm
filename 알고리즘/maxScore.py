class MaxAlgorithm:
    
    def __init__(self, ns):
        
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0
        
    def setMaxNumIdxAndNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0
        
        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.MaxNum = n
                self.maxNumIdx = i
                
    def getMaxNum(self):
        return self.maxNum
    
    def getMaxNumIdx(self):
        return self.maxNumIdx
    
    