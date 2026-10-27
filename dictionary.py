# Q1
student = {"name": "Rahul","age": 20,"marks": 85}
print("Student details:", student)

# Q2
student = {"name": "Priya","age": 19,"city": "Nagpur"}
print("Student name:", student["name"])
print("Student city:", student["city"])

# Q3
student = {"name": "Amit", "age": 20}
student["course"] = "Python"
print("Updated dictionary:", student)

# Q4
student = {"name": "Neha", "marks": 75}
student["marks"] = 90
print("Updated dictionary:", student)

# Q5
employee = {"name": "Rohan","age": 25,"salary": 30000}
employee.pop("age")
print("Updated dictionary:", employee)

# Q6
student = {"name": "Kiran","age": 21,"marks": 88}
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

# Q7
student = {"name": "Sahil","age": 20,"marks": 80}
if "marks" in student:
    print("Key exists")
else:
    print("Key does not exist")
    
# Q8
marks = {"Maths": 85,"Science": 90,"English": 80}
total = sum(marks.values())
print("Total marks:", total)

# Q9
text = "banana"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print("Character frequency:", frequency)