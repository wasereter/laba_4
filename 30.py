class Student:
    def setYear(self, year):
        self.year = year 
	
    def getYear(self):
        return self.year 
class Employee(Student):
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setSalary(self, salary):
        self.salary = salary
        
    def getSalary(self):
        return self.salary
    
    def setSurname(self, surname):
        self.surname = surname
        
    def getSurname(self):
        return self.surname
        
student = Employee()
student.setName('smad')
student.setSalary(23423)
student.setSurname('ashjfdhkh')
student.setYear(3)
print(student.getYear())
print(student.getName())
print(student.getSalary())
print(student.getSurname())
