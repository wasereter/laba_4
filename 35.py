class User:
	__name = None
	__surname = None
	
	def setName(self,name):
		self.__name = name 
	
	def getName(self):
		return self.__name 
	
	def setSurn(self, surname):
		self.__surname = surname 
	
	def getSurn(self):
		return self.__surname 
		
class Employee(User):
    def getFull(self):
	    return self.__name + ' ' + self.__surname 
    pass
employee = Employee()
employee.setName('Jon')
name = employee.getName()
print(name)
employee.setSurn('Wotson')
print(employee.getSurn())
print(employee.getFull())
