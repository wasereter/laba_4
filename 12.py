class Employee:
    def __init__ (self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
    def show(self):
        print(self.name + " " + self.surname)
    def salar(self):
        print(self.salary)
    def salaryup(self):
        print(self.salary * 1.1)
e = Employee('sergey', 'pribitkov', 24234)
e.show()
e.salar()
e.salaryup()
