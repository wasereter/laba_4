class Employee:
    __name = None
    __surname = None
    __salary = None
    def __init__ (self, name, surname, salary):
        self.__name = name
        self.__surname = surname
        self.__salary = salary
    def show(self):
        print(self.__name + " " + self.__surname)
        print(self.__salary)
e = Employee('sergey', 'pribitkov', 24234)
e.show()
