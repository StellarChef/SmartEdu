class Person:
    def __init__(self, name, surname, info=None):
        self.name = name
        self.surname = surname
        self.info = info if info is not None else {}

class Student(Person):
    def __init__(self, name, surname, id_student, grades=None, info=None):
        super().__init__(name, surname, info)
        self.id_student = id_student
        self.grades = grades if grades is not None else []

    def add_grade(self, subject, value):
        self.grades.append({"subject": subject, "value": value})
        print(f"You added the grade {value} in {subject}")

    def __str__(self):
        return f"{self.name} {self.surname} (ID: {self.id_student})"
    
class Parent(Person):
    def __init__(self,name,surname, id_parent, info):
        super().__init__(name,surname,info)
        self.id_parent = id_parent

