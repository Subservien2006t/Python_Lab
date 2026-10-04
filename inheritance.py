# Q1 
class Employee:
    def __init__(self, employee_id, employee_name, monthly_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.monthly_salary = monthly_salary

    def show_employee(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.employee_name)
        print("Salary:", self.monthly_salary)


class Manager(Employee):
    def __init__(self, employee_id, employee_name, monthly_salary, department_name):
        super().__init__(employee_id, employee_name, monthly_salary)
        self.department_name = department_name

    def show_manager(self):
        self.show_employee()
        print("Department:", self.department_name)
        print("Annual Salary:", self.monthly_salary * 12)


manager_obj = Manager(201, "Karan", 55000, "Finance")
manager_obj.show_manager()

# Q2 
class Vehicle:
    def __init__(self, company_name, vehicle_model):
        self.company_name = company_name
        self.vehicle_model = vehicle_model

    def show_vehicle(self):
        print("Brand:", self.company_name)
        print("Model:", self.vehicle_model)


class Car(Vehicle):
    def __init__(self, company_name, vehicle_model, fuel, original_price):
        super().__init__(company_name, vehicle_model)
        self.fuel = fuel
        self.original_price = original_price

    def show_car(self):
        self.show_vehicle()
        print("Fuel Type:", self.fuel)
        print("Price:", self.original_price)

    def calculate_discount(self):
        discount_amount = self.original_price * 0.10
        reduced_price = self.original_price - discount_amount
        print("Discounted Price:", reduced_price)


car_obj = Car("Honda", "City", "Petrol", 1500000)
car_obj.show_car()
car_obj.calculate_discount()

# Q4 
class PersonalDetails:
    def __init__(self, person_name, person_age):
        self.person_name = person_name
        self.person_age = person_age


class ProfessionalDetails:
    def __init__(self, employee_number, job_title, monthly_income):
        self.employee_number = employee_number
        self.job_title = job_title
        self.monthly_income = monthly_income


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, person_name, person_age, employee_number, job_title, monthly_income):
        PersonalDetails.__init__(self, person_name, person_age)
        ProfessionalDetails.__init__(
            self, employee_number, job_title, monthly_income
        )

    def show_details(self):
        print("Name:", self.person_name)
        print("Age:", self.person_age)
        print("Employee ID:", self.employee_number)
        print("Designation:", self.job_title)
        print("Salary:", self.monthly_income)


employee_obj = Employee("Rohan", 24, 202, "Software Engineer", 60000)
employee_obj.show_details()

# Q7
class Shape:
    def display_shape(self):
        print("This is a shape")


class Circle(Shape):
    def find_area(self, radius_value):
        circle_area = 3.14 * radius_value * radius_value
        print("Circle Area:", circle_area)


class Rectangle(Shape):
    def find_area(self, length_value, width_value):
        rectangle_area = length_value * width_value
        print("Rectangle Area:", rectangle_area)


class Triangle(Shape):
    def find_area(self, base_value, height_value):
        triangle_area = 0.5 * base_value * height_value
        print("Triangle Area:", triangle_area)


circle_obj = Circle()
circle_obj.display_shape()
circle_obj.find_area(7)

rectangle_obj = Rectangle()
rectangle_obj.display_shape()
rectangle_obj.find_area(12, 6)

triangle_obj = Triangle()
triangle_obj.display_shape()
triangle_obj.find_area(8, 5)

# Q8 
class Employee:
    def __init__(self, staff_id, staff_name, base_salary):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.base_salary = base_salary


class Manager(Employee):
    def calculate_salary(self):
        manager_allowance = self.base_salary * 0.30
        return self.base_salary + manager_allowance


class Developer(Employee):
    def calculate_salary(self):
        developer_allowance = self.base_salary * 0.20
        return self.base_salary + developer_allowance


class Tester(Employee):
    def calculate_salary(self):
        tester_allowance = self.base_salary * 0.15
        return self.base_salary + tester_allowance


manager = Manager(301, "Vivek", 60000)
developer = Developer(302, "Arjun", 45000)
tester = Tester(303, "Neeraj", 38000)

print("Manager Salary:", manager.calculate_salary())
print("Developer Salary:", developer.calculate_salary())
print("Tester Salary:", tester.calculate_salary())

# Q10
class Vehicle:
    def __init__(self, company):
        self.company = company


class Car(Vehicle):
    def __init__(self, company, car_model):
        super().__init__(company)
        self.car_model = car_model


class Bike(Vehicle):
    def __init__(self, company, bike_model):
        super().__init__(company)
        self.bike_model = bike_model


class SportsCar(Car):
    def show_car(self):
        print("Sports Car")
        print("Brand:", self.company)
        print("Model:", self.car_model)
        print("Type: High Performance")


class ElectricBike(Bike):
    def show_bike(self):
        print("Electric Bike")
        print("Brand:", self.company)
        print("Model:", self.bike_model)
        print("Type: Electric")


sports_car = SportsCar("Audi", "R8")
sports_car.show_car()

print()

electric_bike = ElectricBike("Ola", "S1 Pro")
electric_bike.show_bike()

# Q11 
class Student:
    def __init__(self, student_roll, student_name, student_course):
        self.student_roll = student_roll
        self.student_name = student_name
        self.student_course = student_course


class Result(Student):
    def __init__(self, student_roll, student_name, student_course,
                 subject_one, subject_two, subject_three):

        super().__init__(student_roll, student_name, student_course)

        self.subject_one = subject_one
        self.subject_two = subject_two
        self.subject_three = subject_three

    def show_result(self):

        total_marks = (
            self.subject_one +
            self.subject_two +
            self.subject_three
        )

        percentage_value = total_marks / 3

        if percentage_value >= 75:
            grade_value = "A"
        elif percentage_value >= 60:
            grade_value = "B"
        elif percentage_value >= 50:
            grade_value = "C"
        else:
            grade_value = "D"

        print("Roll No:", self.student_roll)
        print("Name:", self.student_name)
        print("Course:", self.student_course)
        print("Total Marks:", total_marks)
        print("Percentage:", percentage_value)
        print("Grade:", grade_value)


result_obj = Result(
    205,
    "Kunal",
    "Computer Science",
    85,
    78,
    92
)

result_obj.show_result()

# Q14 
class Camera:
    def capture_photo(self):
        print("Photograph captured")


class Phone:
    def call_number(self):
        print("Calling a number")


class Smartphone(Camera, Phone):
    def show_features(self):
        print("Smartphone supports camera and calling features")


smartphone_obj = Smartphone()

smartphone_obj.show_features()
smartphone_obj.capture_photo()
smartphone_obj.call_number()

# Q17 
class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def eat_food(self):
        print(self.animal_name, "is eating")


class Dog(Animal):
    def make_sound(self):
        print(self.animal_name, "says Woof")


class Cat(Animal):
    def make_sound(self):
        print(self.animal_name, "says Meow")


class Cow(Animal):
    def make_sound(self):
        print(self.animal_name, "says Moo")


dog_obj = Dog("Dog")
dog_obj.eat_food()
dog_obj.make_sound()

print()

cat_obj = Cat("Cat")
cat_obj.eat_food()
cat_obj.make_sound()

print()

cow_obj = Cow("Cow")
cow_obj.eat_food()
cow_obj.make_sound()