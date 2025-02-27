class Employee:
    def show(self, name, salary):
        return name + " " + salary
    pass
employee = Employee()
print(employee.show('Max', '63456'))
