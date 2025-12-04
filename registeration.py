from person import Person, Parent, Student

def register_student():
    # Collect input data
    mother_first = input("Mother's first name: ")
    mother_last = input("Mother's last name: ")
    father_first = input("Father's first name: ")
    father_last = input("Father's last name: ")

    student_first = input("Student's first name: ")
    student_last = input("Student's last name: ")
    pesel_student = input("Student's PESEL: ")
    illnesses = input("Student's illnesses (optional): ")

    # Create objects
    student = Student(student_first, student_last, pesel_student, info={"illnesses": illnesses})
    mother = Parent(mother_first, mother_last)
    father = Parent(father_first, father_last)

    # Link parents to student
    student.add_parent(mother)
    student.add_parent(father)

    print("✅ Student and parents registered successfully!")
    print("Student:", student)
    print("Parents:", ", ".join(str(p) for p in student.parents))

    return student
