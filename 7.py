class Employee:
    name = None
    salary = 0

    def show(self):
        print(self.name)

    def show_sal(self):
        print(self.salary)


employee = Employee()
employee.name = 'john'
employee.salary = 34652
employee.show()
employee.show_sal()
