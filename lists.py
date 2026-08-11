#Q1
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Fruits:", fruits)

#Q2
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])

#Q3
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
colors[2] = "Orange"
print("Updated list:", colors)

#Q4
numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.insert(0, 5)
numbers.insert(3, 25)
print("Updated list:", numbers)

#Q5
students = ["Rahul", "Amit", "Sneha", "Priya", "Rohan"]
students.pop(0)
students.pop()
students.remove("Sneha")
print("Remaining students:", students)

#Q6
numbers = [25, 10, 45, 5, 30]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)

#Q7
numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)

#Q8
numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 19, 20, 31, 42, 53, 64]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)

#Q9
cities = ["Mumbai", "Pune", "Nashik", "Kolhapur", "Nagpur"]
city = input("Enter city name: ")
if city in cities:
    print("City exists in the list.")
else:
    print("City does not exist in the list.")
    
#Q10
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print("Original:", numbers)          
print("Reversed:", reversed_numbers)

#Q11
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list:", numbers[::-1])

#Q12
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i])

#Q15
numbers = [10, 25, 45, 30, 50, 40]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
unique.sort()
print("Second largest:", unique[-2])

#Q16
students = [["Rahul", 101, 85],["Amit", 102, 90],["Sneha", 103, 88],["Priya", 104, 92]]
for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()
    
#Q23
numbers = [10, 20, 10, 30, 20, 10, 40]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("Frequency:", frequency)

#Q25
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List after removing duplicates:", unique)

