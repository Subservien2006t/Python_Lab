# Q1
number = int(input("Enter a number: "))
if number == 0:
    print("The number is zero.")
else:
    print("The number is not zero.")

# Q2
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
if first > second:
    print("The first number is greater.")
else:
    print("The second number is greater.")

# Q3
value = int(input("Enter a number: "))
if value >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# Q4
letter = input("Enter a character: ")
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

# Q5
marks = float(input("Enter percentage: "))

if marks >= 90:
    print("Excellent Performance")
elif marks >= 80:
    print("Very Good Performance")
elif marks >= 70:
    print("Good Performance")
elif marks >= 60:
    print("Average Performance")
else:
    print("Poor Performance")

# Q6
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
third_num = int(input("Enter third number: "))

if first_num >= second_num and first_num >= third_num:
    print("The first number is the largest.")
elif second_num >= first_num and second_num >= third_num:
    print("The second number is the largest.")
else:
    print("The third number is the largest.")

# Q7
value1 = int(input("Enter first number: "))
value2 = int(input("Enter second number: "))
value3 = int(input("Enter third number: "))

if value1 <= value2 and value1 <= value3:
    print("The first number is the smallest.")
elif value2 <= value1 and value2 <= value3:
    print("The second number is the smallest.")
else:
    print("The third number is the smallest.")

# Q8
digit = int(input("Enter a number: "))
if digit % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Q9
input_year = int(input("Enter a year: "))
if (input_year % 400 == 0) or (input_year % 4 == 0 and input_year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Q10
status = input("Married? (yes/no): ")
person_gender = input("Gender (male/female): ")
driver_age = int(input("Enter age: "))

if status == "yes":
    print("Driver is Insured")
elif status == "no" and person_gender == "male" and driver_age > 30:
    print("Driver is Insured")
elif status == "no" and person_gender == "female" and driver_age > 25:
    print("Driver is Insured")
else:
    print("Driver is Not Insured")