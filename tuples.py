#Q1
t = (1, 2, 3, 4, 5)
print(t)

#Q2
t = ("Mumbai", "Delhi", "Bangalore", "Chennai","Kolkata")
print(t[0])
print(t[-1])
print(t[2])

#Q3
t = ("Yash", "Ravi", "Amit", "Suresh", "Rahul")
print(len(t))

#Q4
t = ("Red", "Green", "Blue", "Yellow", "Orange")
print("Red" in t)

#Q5
t = ("Apple", "Banana", "Cherry")
for i in t:
    print(i)
    
#Q6
t = (11,11,23,123,13)
count = t.count(11)
print(count)

#Q7
employee_ids = (101, 102, 103, 104, 105)
id = int(input("Enter employee ID: "))
if id in employee_ids:
    print("Index:", employee_ids.index(id))
else:
    print("ID not found")

#Q8
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
result = tuple1 + tuple2
print("Concatenated tuple:", result)

#Q10
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("First five:", numbers[:5])
print("Last five:", numbers[5:])
print("Middle four:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])

#Q11
t = (10, 20, 30, 40)
numbers = list(t)
numbers.append(50)
print("List:", numbers)

#Q12
numbers = []
for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)
t = tuple(numbers)
print("Tuple:", t)

#Q14
t = (10, 20, 30, 40)
print("Tuple:", t)
del t
print("Tuple deleted successfully")

#Q16
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
total = sum(numbers)
print("Sum:", total)

#Q18
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
total = sum(numbers)
print("Average:", total / 10)

#Q19
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150)
cntodd = 0
cnteven = 0
for num in numbers:
    if num % 2 == 0:
        cnteven += 1
    else:
        cntodd += 1
print("Even numbers:", cnteven)
print("Odd numbers:", cntodd)

#Q21
info = []
rn = int(input("Enter a roll no: "))
name = input("Enter a name: ")
dept = input("Enter a department: ")
mark = int(input("Enter mark: "))
info.append((rn, name, dept, mark))
t = tuple(info)
print("Information: ", t)

#Q28
t = (10, 20, 30, 20, 40, 10, 50)
frequency = {}
for item in t:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Frequency of each element:", frequency)