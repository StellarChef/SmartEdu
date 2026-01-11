class Person:
    def __init__(self,first_name,last_name,age ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Student(Person):
    def __init__(self,first_name,last_name,age,student_id,student_group):
        super().__init__(first_name,last_name,age)
        self.student_id = student_id
        self.student_group = student_group

class Parent(Person):
    def __init__(self,first_name,last_name,age,child):
        super().__init__(first_name,last_name,age)
        self.child = child
