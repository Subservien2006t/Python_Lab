# Q1
import numpy as np

data = np.array([15, 25, 35, 45, 55, 65, 75, 85, 95, 105])

print("Array:", data)
print("Size:", data.size)
print("Data Type:", data.dtype)
print("Number of Dimensions:", data.ndim)

# Q2
import numpy as np

first_array = np.array([12, 24, 36, 48, 60])
second_array = np.array([2, 3, 4, 6, 10])

print("Addition:", first_array + second_array)
print("Subtraction:", first_array - second_array)
print("Multiplication:", first_array * second_array)
print("Division:", first_array / second_array)
print("Modulus:", first_array % second_array)

# Q3
import numpy as np

numbers_list = np.array([18, 22, 9, 41, 35, 16, 55, 29, 13, 38])

print("Array:", numbers_list)
print("Maximum:", np.max(numbers_list))
print("Minimum:", np.min(numbers_list))
print("Sum:", np.sum(numbers_list))
print("Average:", np.mean(numbers_list))

# Q4
import numpy as np

number_series = np.arange(1, 21)

even_list = number_series[number_series % 2 == 0]
odd_list = number_series[number_series % 2 != 0]

print("Array:", number_series)
print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)

# Q5
import numpy as np

sequence = np.arange(1, 13)

print("Original Array:")
print(sequence)

print("\n2 x 6 Matrix:")
print(sequence.reshape(2, 6))

print("\n3 x 4 Matrix:")
print(sequence.reshape(3, 4))

print("\n4 x 3 Matrix:")
print(sequence.reshape(4, 3))

# Q6
import numpy as np

first_matrix = np.array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
])

second_matrix = np.array([
    [18, 16, 14],
    [12, 10, 8],
    [6, 4, 2]
])

sum_matrix = first_matrix + second_matrix

print("Matrix 1:")
print(first_matrix)

print("Matrix 2:")
print(second_matrix)

print("Matrix Addition:")
print(sum_matrix)

# Q8
import numpy as np

table = np.array([
    [2, 4, 6, 8],
    [10, 12, 14, 16],
    [18, 20, 22, 24]
])

print("Original Matrix:")
print(table)

print("Transpose:")
print(table.T)

# Q12
import numpy as np

scores = np.array([25, 70, 40, 85, 30, 95, 15, 60, 45, 80])

print("Original Array:", scores)

scores[scores > 50] = 0

print("Updated Array:", scores)

# Q13
import numpy as np

values = np.array([52, 18, 91, 27, 63, 7, 39])

ascending_values = np.sort(values)
descending_values = np.sort(values)[::-1]

print("Original Array:", values)
print("Ascending Order:", ascending_values)
print("Descending Order:", descending_values)

# Q14
import numpy as np

duplicate_data = np.array([15, 25, 15, 35, 25, 45, 35, 55, 45, 15])

distinct_values = np.unique(duplicate_data)

print("Original Array:", duplicate_data)
print("Unique Elements:", distinct_values)

# Q15
import numpy as np

student_marks = np.array([72, 86, 69, 94, 77, 83, 91, 65, 88, 79])

print("Marks:", student_marks)
print("Highest Marks:", np.max(student_marks))
print("Lowest Marks:", np.min(student_marks))
print("Average Marks:", np.mean(student_marks))
print("Median:", np.median(student_marks))
print("Standard Deviation:", np.std(student_marks))