limit = 50

# Q1
count = 1
while count <= limit:
    print(count)
    count += 1

# Q2
value = 1
while value <= limit:
    if value % 2 == 0:
        print(value)
    value += 1

# Q3
value = 1
while value <= limit:
    if value % 2 != 0:
        print(value)
    value += 1

# Q4
total = 0
value = 1
while value <= limit:
    total += value
    value += 1
print(total)

# Q5
odd_sum = 0
value = 1
while value <= limit:
    if value % 2 != 0:
        odd_sum += value
    value += 1
print(odd_sum)

# Q6
even_sum = 0
value = 1
while value <= limit:
    if value % 2 == 0:
        even_sum += value
    value += 1
print(even_sum)

# Q7
value = limit
while value >= 1:
    print(value)
    value -= 1

# Q8
first = 0
second = 1
while first <= limit:
    print(first)
    first, second = second, first + second

# Q9
number = int(input("Enter a number: "))
fact = 1
while number > 0:
    fact *= number
    number -= 1
print("Factorial:", fact)

# Q10
check_num = int(input("Enter a number: "))
prime = True

if check_num <= 1:
    prime = False
else:
    divisor = 2
    while divisor * divisor <= check_num:
        if check_num % divisor == 0:
            prime = False
            break
        divisor += 1

if prime:
    print(check_num, "is a prime number")
else:
    print(check_num, "is not a prime number")

# Q11
digit_num = int(input("Enter a number: "))
digit_sum = 0

while digit_num > 0:
    digit_sum += digit_num % 10
    digit_num //= 10

print("Sum of digits:", digit_sum)

# Q12
pal_num = int(input("Enter a number: "))
original = pal_num
reverse = 0

while pal_num > 0:
    rem = pal_num % 10
    reverse = reverse * 10 + rem
    pal_num //= 10

if original == reverse:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")

# Q13
rev_num = int(input("Enter a number: "))
answer = 0

while rev_num > 0:
    rem = rev_num % 10
    answer = answer * 10 + rem
    rev_num //= 10

print("Reversed number:", answer)