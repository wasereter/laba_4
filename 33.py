class User:
	def __init__(self,name, surname):
		self.name = name 
		self.surname = surname 
	
	def getName(self):
		return self.name 
	
	def getSurn(self):
		return self.surname 
class Employee(User):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def setSalary(self, salary):
        self.salary = salary
        
    def getSalary(self):
        return self.salary
        
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
em = Employee('dfsfds','dsfsd')
print(em.getName())
print(em.getSurn())
em.setAge(43)
em.setSalary(323423)
print(em.getAge())
print(em.getSalary())
