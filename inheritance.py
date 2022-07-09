from classes import Calculator

class ChildImp1(Calculator):
    num2 = 200

    def __init__(self, a, b):
        super().__init__(a, b)  
        # can also be done with Calculator.__init__(self,a,b)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = ChildImp1(4,5)
print(obj.getCompleteData())