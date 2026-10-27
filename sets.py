# Q1
set1 = {10, 20, 30, 40, 50}
print("Set elements:", set1)

# Q2
numbers = {10, 20, 30, 40}
numbers.add(50)
print("Updated set:", numbers)

# Q3
colors = {"Red", "Blue", "Green", "Yellow"}
colors.remove("Blue")
print("Updated set:", colors)

# Q4
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
result = set_a.union(set_b)
print("Union:", result)

# Q5
set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}
result = set_a.intersection(set_b)
print("Intersection:", result)

# Q6
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5}
result = set_a.difference(set_b)
print("Difference:", result)

# Q7
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
result = set_a.symmetric_difference(set_b)
print("Symmetric difference:", result)

# Q8
set_a = {2, 4}
set_b = {2, 4, 6, 8, 10}
print("Is subset:", set_a.issubset(set_b))

# Q9
numbers = [10, 20, 10, 30, 20, 40, 50, 30]
unique_numbers = set(numbers)
print("Unique elements:", unique_numbers)
print("Total unique elements:", len(unique_numbers))