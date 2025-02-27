class Employee:
    __name = None
    __salary = 0
    __age = 0

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getSalary(self):
        return self.__salary

    def getName(self):
        return self.__name

    def getage(self):
        return self.__age


employee = Employee('max', 23454, 27)
print(employee.getSalary())
print(employee.getage())
print(employee.getName())
