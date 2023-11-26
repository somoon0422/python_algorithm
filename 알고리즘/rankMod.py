class RankDeviation:
    
    def __init__(self, mss , ess):
        self.midStuScos = mss
        self.endStuScos = ess
        self.midRanks = [0 for i in range(len(mss))]
        self.endRanks = [0 for i in range(len(mss))]
        self.rankDeviation = [0 for i in range(len(mss))]
        
    
    def setRank(self, ss, rs):
        for idx, sco1 in enumerate(ss):
            for sco2 in ss:
                if sco1 < sco2:
                    rs[idx] += 1
                    
    def setMidRank(self):
        self.setRank(self.midStuScos, self.midRanks)
        
    def getMidRank(self):
        return self.midRanks
        
    def setEndRank(self):
        self.setRank(self.endStuScos, self.endRanks)
        
    def getEndRank(self):
        return self.endRanks
    
    def printRankDeviation(self):
        
        for idx, mRank in enumerate(self.midRanks):
            deviation = mRank - self.endRanks[idx]
            
            if deviation > 0:
                deviation = '↑' + str(abs(deviation))
                
            elif deviation < 0 :
                deviation = '↓' + str(abs(deviation))
                
            else:
                deviation = '=' + str(abs(deviation))
            
            print( f'mid_rank: {mRank} \t end_rank: {self.endRanks[idx]} \t Deviation: {deviation} ')
            
            
            