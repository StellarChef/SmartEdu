class School:
    def __init__(self,name=str, subjects=None, schoolclasses=None, teachers = None):
        self.name = name
        self.subjects = subjects if subjects is not None else []
        self.schoolclasses = schoolclasses  if schoolclasses is not None else []
        self.teachers = teachers if teachers is not None else []
    def add_subject(self,subject):
        self.subjects.append(subject)
        print(f"You added a new subject names {subject}")

    def add_classes(self, id, students=None):
        new_class = School_Class(id)
        
        print(f"You added a class {id}")


    def __str__(self):
        result = f"{self.name}\n"
        result += "=" * 30 + "\n"
        result += "=" * 30 + "Classes" + "=" * 30 + "\n"
        for c in self.schoolclasses:
            result += f"{c}\n"
        return result
    
class School_Class:
    def __init__(self, id):
        self.id = id
        self.students = []
        self.timetable = None

    def sort_class(self):
        sorted(self.students)

    def add_student(self, name, surname):
        class_number = len(self.students) + 1
        student_id = f"{self.id}-{class_number}"
        self.students.append(Student(name,surname,student_id,[]))
        print(f"You added a {name} to {self.id}")

    def __str__(self):
        result = f"{self.id} " + f"{len(self.students)}" + "\n"
        for idx, s in enumerate(self.students, start=1):
            result += f"{idx}. " + f"{s}\n"
        return result

class Subject:
    def __init__(self, name, level=None):
        self.name = name
        self.level = level  # np. "primary", "secondary"
        self.grades = {}    # klucz: student_id, wartość: lista ocen

    def add_grade(self, student_id, value):
        if student_id not in self.grades:
            self.grades[student_id] = []
        self.grades[student_id].append(value)
        print(f"Dodałeś ocenę {value} z {self.name} dla studenta {student_id}")

    def __str__(self):
        result = f"Subject: {self.name} ({self.level})\n"
        for student_id, grades in self.grades.items():
            result += f"Student {student_id}: {grades}\n"
        return result

    
class Student:
    def __init__(self,name,surname, id_student, grades=None):
        self.name = name
        self.surname = surname
        self.id_student = id_student
        self.grades = grades if grades is not None else []

    def add_grade(self, grade, value):
        self.grades.append(grade)
        print(f"You added the grade {grade} of value {value}")

    def __str__(self):
        result = f"{self.name} {self.surname}"
        return result


