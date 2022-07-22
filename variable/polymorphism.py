class Employee:
    def setnumberofworkinghours(self):
        self.setnumberofworkinghours=40

    def displaythenumberofworkinghours(self):
        print(self.numberofworkinghours)

class Trainee(Employee):

      def setnumberofworkinghours(self):
        self.numberofworkinghours = 45

employee = Employee()
employee.setnumberofworkinghours()
print("number of working hours of the employee:",end='')
employee.displaythenumberofworkinghours()




