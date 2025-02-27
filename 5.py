class Employee:
    def show(self):
        return 'Hello world!'
    pass
employee = Employee()
employee.name = 'Max'
employee.salary = 35000
print(employee.show())
