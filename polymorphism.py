# Q1 
class FigureQ1:
    def find_area(self):
        print("Area of figure")


class CircleQ1(FigureQ1):
    def find_area(self):
        radius_value = 7
        print("Circle Area:", 3.14 * radius_value * radius_value)


class RectangleQ1(FigureQ1):
    def find_area(self):
        length_value = 12
        width_value = 6
        print("Rectangle Area:", length_value * width_value)


class TriangleQ1(FigureQ1):
    def find_area(self):
        base_value = 10
        height_value = 8
        print("Triangle Area:", 0.5 * base_value * height_value)


figure_list = [CircleQ1(), RectangleQ1(), TriangleQ1()]

for figure in figure_list:
    figure.find_area()

# Q2 
class WorkerQ2:
    def find_salary(self):
        print("Worker salary")


class ManagerQ2(WorkerQ2):
    def find_salary(self):
        basic_pay = 55000
        extra_allowance = basic_pay * 0.30
        print("Manager Salary:", basic_pay + extra_allowance)


class ProgrammerQ2(WorkerQ2):
    def find_salary(self):
        basic_pay = 45000
        extra_allowance = basic_pay * 0.20
        print("Programmer Salary:", basic_pay + extra_allowance)


class TesterQ2(WorkerQ2):
    def find_salary(self):
        basic_pay = 38000
        extra_allowance = basic_pay * 0.15
        print("Tester Salary:", basic_pay + extra_allowance)


worker_list = [ManagerQ2(), ProgrammerQ2(), TesterQ2()]

for worker in worker_list:
    worker.find_salary()

# Q3
class TransportQ3:
    def begin(self):
        print("Transport is starting")


class CarQ3(TransportQ3):
    def begin(self):
        print("Car starts with a key")


class BikeQ3(TransportQ3):
    def begin(self):
        print("Bike starts with a self-start button")


class BusQ3(TransportQ3):
    def begin(self):
        print("Bus starts with a large engine")


transport_list = [CarQ3(), BikeQ3(), BusQ3()]

for transport in transport_list:
    transport.begin()

# Q4
class CreatureQ4:
    def make_sound(self):
        print("Creature makes a sound")


class DogQ4(CreatureQ4):
    def make_sound(self):
        print("Dog says Woof")


class CatQ4(CreatureQ4):
    def make_sound(self):
        print("Cat says Meow")


class CowQ4(CreatureQ4):
    def make_sound(self):
        print("Cow says Moo")


class LionQ4(CreatureQ4):
    def make_sound(self):
        print("Lion says Roar")


creature_list = [DogQ4(), CatQ4(), CowQ4(), LionQ4()]

for creature in creature_list:
    creature.make_sound()

# Q8 
class DocumentReportQ8:
    def create(self):
        print("Creating report")


class PDFDocumentQ8(DocumentReportQ8):
    def create(self):
        print("Creating PDF Report")


class ExcelDocumentQ8(DocumentReportQ8):
    def create(self):
        print("Creating Excel Report")


class HTMLDocumentQ8(DocumentReportQ8):
    def create(self):
        print("Creating HTML Report")


def make_report(report_file):
    report_file.create()


make_report(PDFDocumentQ8())
make_report(ExcelDocumentQ8())
make_report(HTMLDocumentQ8())

# Q10
class LearnerQ10:
    def __init__(self, student_name, score):
        self.student_name = student_name
        self.score = score

    def __gt__(self, another_student):
        return self.score > another_student.score

    def __lt__(self, another_student):
        return self.score < another_student.score


learner_one = LearnerQ10("Rohan", 88)
learner_two = LearnerQ10("Vikas", 72)

if learner_one > learner_two:
    print(learner_one.student_name, "has higher marks")

if learner_one < learner_two:
    print(learner_one.student_name, "has lower marks")

# Q11 
class ItemQ11:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def __eq__(self, another_item):
        return self.item_price == another_item.item_price

    def __gt__(self, another_item):
        return self.item_price > another_item.item_price


item_one = ItemQ11("Tablet", 45000)
item_two = ItemQ11("Headphones", 12000)

if item_one == item_two:
    print("Both items have the same price")
else:
    print("Items have different prices")

if item_one > item_two:
    print(item_one.item_name, "is more expensive")

# Q13 
class HumanQ13:
    def show_role(self):
        print("Human")


class StudentQ13(HumanQ13):
    def show_role(self):
        print("Role: Student")


class TeacherQ13(HumanQ13):
    def show_role(self):
        print("Role: Teacher")


class AdminQ13(HumanQ13):
    def show_role(self):
        print("Role: Administrator")


person_list = [
    StudentQ13(),
    TeacherQ13(),
    AdminQ13()
]

for person_obj in person_list:
    person_obj.show_role()