limit = 10

# Q1
for count in range(1, limit + 1):
    print(count)

# Q2
for number in range(1, limit + 1):
    if number % 2 == 0:
        print(number)

# Q3
for number in range(1, limit + 1):
    if number % 2 != 0:
        print(number)

# Q4
for power in range(1, limit + 1):
    result = 2 ** power
    if result > limit:
        break
    print(result)

# Q8
for row in range(3):
    print("A B C")

# Q9
size = int(input("Enter a number: "))
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for row in range(1, size + 1):
    for col in range(row):
        print(alphabets[col], end="")
    print()

# Q10
rows = int(input("Enter a number: "))
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for row in range(rows, 0, -1):
    for col in range(row):
        print(chars[col], end="")
    print()

# Q11
rows1 = int(input("Enter a number: "))

for row in range(1, rows1 + 1):
    for col in range(1, row + 1):
        print(col, end="")
    print()

# Q12
rows2 = int(input("Enter a number: "))

for row in range(1, rows2 + 1):
    for col in range(1, row + 1):
        print(row, end="")
    print()