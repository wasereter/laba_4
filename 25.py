class Employee:
  __name = None
  __salary = 0

  def __init__(self,name,salary):
    self.__name = name
    self.__salary = salary

  def getName(self):
    return self.__name
    
class EmployeeCollection:

    def __init__(self):
        self.__name = []
        self.__salary = []

    def add(self,user, value):
        self.__name.append(user)
        self.__salary.append(value)

    def show(self):
        for user in self.__name:
            print(user)
      
    def showSalary(self):
            print(sum(self.__salary))
    def midsalary(self):
            summa = sum(self.__salary)
            print(summa/len(self.__name))
uc = EmployeeCollection()
uc.add('john', 23215) 
uc.add('eric', 54784) 
uc.add('kyle', 62346) 
uc.show() 
uc.showSalary()
uc.midsalary()
