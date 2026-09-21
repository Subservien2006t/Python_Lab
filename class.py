#q1

class student:
    def __init__(self,rno,name,marks):
        self.rno =rno
        self.name=name
        self.marks=marks
    def display(self):
        print("roll number: (self.rno)")
        print("name: (self.name)")
        print("marks: (self.marks)")
obj1 =student(849, "shraddha kole",89)
obj1.display()


#q2
class rectangle:
   def __init__(self,lenght, breadth):
       self.lenght=lenght
       self.breadth=breadth
   def area(self):
       return self.lenght * self.breadth
   def perimeter(self):
       return 2 * (self.lenght+ self.breadth)
obj2 =rectangle(8,9)
print("area of rectangle: ", obj2.area())
print("perimeter of rectangle:", obj2.perimeter())


#q3
class circle:  
   def __init__(self,radius):
       self.radius=radius
   def area(self): 
       return 3.14* self.radius*self.radius
   def circumference(self):
       return 2*3.14* self.radius
obj3= circle(4)  
print("area of circle", obj3.area())
print("circumference of circle:", obj3.circumference())
          

#Q4
class Book:
    def __init__(self, bid, title, author, price):
        self.bid = bid
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print(f"Book ID: {self.bid}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
obj4 = Book(1, "Python Programming", "John Doe", 500)
obj4.display()

#Q5
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")
        print(f"Price: ${self.price}")
    def apply_discount(self, discount_percentage):
        discount_amount = (discount_percentage / 100) * self.price
        self.price -= discount_amount
obj5 = MobilePhone("Apple", "iPhone 13", 128, 999999)
obj5.apply_discount(10)
obj5.display()        

#Q6
class Patient:
    def __init__(self, pid, name, age, disease, fee):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee
    def display(self):
        print(f"Patient ID: {self.pid}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")
        print(f"Fee: {self.fee}")
    def total_fee(self, additional_fee):
        self.fee += additional_fee
obj6 = Patient(1, "Alice", 30, "Flu", 100)
obj6.total_fee(50)
obj6.display()


#q7
class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate, availability):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability
    def rent(self):
        if self.availability:
            self.availability = False
            return True
        else:
            return False
    def return_vehicle(self):
        self.availability = True
    def calculate_rental_charges(self, days):
        return self.rental_rate * days
obj7 = Vehicle("MH12AB1234", "Toyota Camry", 1000, True)
if obj7.rent():
    print("Vehicle rented successfully.")
    charges = obj7.calculate_rental_charges(5)
    print(f"Rental charges for 5 days: {charges}")
    obj7.return_vehicle()
    print("Vehicle returned successfully.")