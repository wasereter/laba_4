class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def capitalize_first_letter(self, string):
        return string[0].upper() + string[1:]

    def get_initials(self):
        name_initial = self.capitalize_first_letter(self.name)
        surname_initial = self.capitalize_first_letter(self.surname)
        return f"{name_initial[0]}.{surname_initial[0]}."

student = Student("ivan", "ivanov")
print(student.get_initials())
