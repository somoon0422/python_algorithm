def getNearNum (an):
    
    bascores = [95,85,75,65,55]
    nearNum = 0
    minNum = 100
    
    for n in bascores:
        absNum = abs(n - an)
        if absNum < minNum:
            minNum = absNum
            nearNum = n
            
    if nearNum == 95:
        return 'A'
    elif nearNum == 85:
        return 'B'
    elif nearNum == 75:
        return 'C'
    elif nearNum == 65:
        return 'D'
    elif nearNum <= 55:
        return 'E'
        
    