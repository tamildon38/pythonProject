class Employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 40

    def displaythenumberworkinghours(self):
        print(self.numberofworkinghours)

class Trainee(Employee):

    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45

    def resetnumberofworkinghours(self):
        super().setnumberofworkinghours()

employee = Employee()
employee.setnumberofworkinghours()
print("number of working hours of the employee:", end='')
employee.displaythenumberworkinghours()

trainee = Trainee()
trainee.setnumberofworkinghours()
print("number of working hours of the trainee:", end='')
trainee.displaythenumberworkinghours()
trainee.resetnumberofworkinghours()
print("number of working hours has been reset:",end='')
trainee.displaythenumberworkinghours()



