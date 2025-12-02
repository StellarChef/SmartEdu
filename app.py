from school import School, School_Class, Student

class Application:
    def run(self):
        self.display()
    def display(self):
        sub = ["math","physics","biology","geography","history","art"]
        classes = [School_Class("1A")]
        classes[0].add_student("Alice", "Smith")
        classes[0].add_student("Bob", "Johnson")
        classes[0].add_student("Alan", "Brown")
        classes[0].add_student("Stachu", "Kowalski")
        classes[0].add_student("Kein", "Müller")
        classes[0].add_student("Rabin", "Levi")
        classes[0].add_student("Maria", "Nowak")
        classes[0].add_student("Tomasz", "Wiśniewski")
        classes[0].add_student("Julia", "Zielińska")
        classes[0].add_student("Oskar", "Dąbrowski")
        Oskar = classes[0].students[-1]

        teachers = []
        smart_people = School("Mądrzy_ludzie",sub, classes, teachers)
        smart_people.add_classes("1B")

        print(smart_people)
        print(Oskar.id_student)
