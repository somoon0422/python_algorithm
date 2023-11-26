class NewGenerationPC:
    
    def __init__(self, name, cpu, memory, ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd
        
    def doExcel(self):
        print('Excel run!')
    
    def doPhotoshop(self):
        print('Photoshop run!')
        
    def printPCInfo(self):
        print(self.name)
        print(self.cpu)
        print(self.memory)
        print(self.ssd)
        

mypc = NewGenerationPC('myPC', 'i5', '16G' , '256G')
mypc.printPCInfo()
        