#Q1
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
num1 = int(input("Enter a number: "))
print("Factorial of", num1, "is", fact(num1))

#Q2
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
num2 = int(input("Enter a number: "))
print(num2, "is", check_even_odd(num2))

#Q3
def greater_of_two(a, b):
    if a > b:
        return a
    else:
        return b
num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))
print("Greater of", num3, "and", num4, "is", greater_of_two(num3, num4))

#Q5
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num5 = int(input("Enter a number: "))
print(num5, "is", "prime" if is_prime(num5) else "not prime")

#Q6
def ar_circle(r):
    return 3.14 * r * r
num6 = int(input("Enter radius: "))
print("Area of circle with radius ",num6,"is ",ar_circle(num6))

#Q7
def natural_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
n = int(input("Enter n: "))
print("Sum =", natural_sum(n))

#Q8
def power(base, exponent):
    return base ** exponent
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Power =", power(base, exponent))

#Q10
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1
    return count
text = input("Enter a string: ")
print("Number of vowels =", count_vowels(text))

#Q21
def total_bill(prices, quantities, discount):
    total = 0
    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]
    discount_amount = total * discount / 100
    final_bill = total - discount_amount
    return total, discount_amount, final_bill
prices = list(map(float, input("Enter item prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))
discount = float(input("Enter discount percentage: "))
total, discount_amount, final_bill = total_bill(prices, quantities, discount)
print("Total before discount =", total)
print("Discount =", discount_amount)
print("Final Bill =", final_bill)

#Q33
square = lambda x: x * x
n = int(input("Enter number: "))
print("Square =", square(n))

#Q34
cube = lambda x: x * x * x
n = int(input("Enter number: "))
print("Cube =", cube(n))

#Q38
numbers = list(map(int, input("Enter numbers: ").split()))
squares = list(map(lambda x: x * x, numbers))
print("Squares =", squares)

#Q41
numbers = list(map(int, input("Enter numbers: ").split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers =", even_numbers)