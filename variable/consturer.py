class num:
    num1 = 100

    def getdata(self,c,d):
        self.firastnumber = c
        self.secoundnumber = d
        print("hi in a function")

    def summation(self):
        return self.firastnumber + self.secoundnumber + self.thirdnumber + self.fourthnumber + num.num1
    def __init__(self,a,b):
        self.thirdnumber = a
        self.fourthnumber = b
        print("i am first running")


obj = num(10,10)
obj.getdata(40, 40)
print(obj.summation())

obj1 = num(20,20)
obj1.getdata(100, 40)
print(obj1.summation())







