def sortNumber(ns, asc=True): #오른차순
    
    #오름차순
    if asc:
        for i in range(len(ns)-1):
            minIdx = i
            
            for j in range(i+1, len(ns)):
                if ns[minIdx] > ns[j]:
                    minIdx = j
                    
            ns[i], ns[minIdx] = ns[minIdx] , ns[i]

    #내림차순
    else:
        for i in range(len(ns)-1):
            minIdx = i
            
            for j in range(i+1, len(ns)):
                if ns[minIdx] < ns[j]:
                    minIdx = j
                    
            ns[i], ns[minIdx] = ns[minIdx] , ns[i] 
                
                
    return ns