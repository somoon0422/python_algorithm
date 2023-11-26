scores = []

def addScore(s):
    scores.append(s)
    
def getScores():
    return scores

def getTotalScore():
    total = 0
    for s in scores:
        total += s
        
    return total

def getAvgScore():
    avg = getTotalScore() / len(scores)
    avg2 = f'{avg:.2f}'
    return avg