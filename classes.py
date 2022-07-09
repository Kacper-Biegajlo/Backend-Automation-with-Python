# classes are user defined blueprints or prototypes

# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__

class Calculator:
    num = 100 # class variable
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("I am called automatically when object is create")


    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.a + self.b + Calculator.num
        


obj = Calculator(2,3) #syntax to create objects in python
obj.getData()
print(obj.Summation())


obj1 = Calculator(4,5)
obj1.getData()
print(obj1.Summation())