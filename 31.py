class Employee:
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age
    def setAge(self, age):
        if 18 < age < 65:
            self.age = age
        else:
            print("Employee age error")
employee = Employee()
employee.setAge(45) 
print(employee.getAge())
