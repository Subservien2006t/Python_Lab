#Q1
import re
text = "My age is 20 and my roll number is 123"
result = re.findall(r'\d', text)
print(result)

#Q2
text = "Apple and ant are amazing animals"
result = re.findall(r'\b[Aa]\w*', text)
print(result)

#Q3
text = input("Enter a string: ")
result = re.findall(r'[aeiouAEIOU]', text)
print("Number of vowels:", len(result))

#Q4
text = "Hello PYTHON World"
result = re.findall(r'[A-Z]', text)
print(result)

#Q5
text = "Hello World\tPython\nProgramming"
result = re.findall(r'[ \t\n]', text)
print("Whitespace characters:", result)
print("Total:", len(result))

#Q6
text = "Hello     World    Python"
result = re.sub(r' +', ' ', text)
print(result)

#Q8
text = "Cats dogs birds and cows"
result = re.findall(r'\b\w+s\b', text, re.IGNORECASE)
print(result)

#Q9
text = "Hello@123! Python# is$ easy."
result = re.sub(r'[^A-Za-z0-9 ]', '', text)
print(result)

#Q10
text = "Python is easy to learn"
result = re.findall(r'\b\w+\b', text)
print("Number of words:", len(result))

#Q12
email = input("Enter email: ")
pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
    
#Q16
password = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9])\S{8,}'
if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")
    
