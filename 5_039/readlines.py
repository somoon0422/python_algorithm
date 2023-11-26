#readlines()
#readline()

uri = './languages.txt'

with open(uri, 'r') as f:
    lanList = f.readline()
        
    while lanList != '':
        print(lanList, end='')
        