class Calculator:
    num=100
    def __init__(self,a,b):
        print("I am called automatically when object of class has called")
        self.a=a
        self.b=b
    def getdata(self):
        print("I am now executing as method in class")
    def add(self):
        return self.a + self.b
c=Calculator(2,3)
c.getdata()
print(c.num)
print(c.add())