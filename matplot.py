
import matplotlib.pyplot as plt
import numpy as np

#line chart
x1 = [1, 2, 3, 4, 5]
y1 = [3, 5, 8, 12, 17]

plt.plot(x1, y1, color="green", linestyle="--")
plt.title("Growth Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

x2 = [1, 2, 3, 4, 5]
y2 = [2, 6, 12, 20, 30]

plt.plot(x2, y2, color="purple", linestyle="-")
plt.title("Square Number Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

#scatter plot
x3 = [4, 6, 9, 8, 3, 15, 5, 10, 7, 12]
y3 = [85, 92, 78, 88, 95, 82, 100, 86, 90, 80]

plt.scatter(x3, y3, color="orange")
plt.title("Student Performance Scatter Plot")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

x4 = [1.2, 1.6, 1.9, 2.2, 2.7, 3.1, 3.6, 4.1, 4.6, 5.2]
y4 = [2.0, 2.8, 3.2, 3.9, 4.3, 5.2, 5.7, 6.1, 6.8, 7.5]

plt.scatter(x4, y4, color="brown")
plt.title("Population vs Income")
plt.xlabel("Population (in billions)")
plt.ylabel("Income (in trillions)")
plt.show()

#bar chart
categories1 = ["P", "Q", "R", "S", "T"]
values1 = [8, 4, 6, 9, 5]

plt.bar(categories1, values1, color="teal")
plt.title("Category Comparison")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

categories2 = ["Item 1", "Item 2", "Item 3", "Item 4"]
values2 = [14, 9, 18, 11]

plt.bar(categories2, values2, color="purple")
plt.title("Item Sales Comparison")
plt.xlabel("Items")
plt.ylabel("Sales")
plt.show()

months = ["Jun", "Jul", "Aug", "Sep", "Oct"]
sales = [110, 140, 100, 160, 125]

plt.barh(months, sales, color="coral")
plt.title("Monthly Sales")
plt.xlabel("Sales")
plt.ylabel("Months")
plt.show()

#pie chart
fruits = ["Mangoes", "Oranges", "Grapes", "Pears"]
fruit_sizes = [35, 20, 25, 20]

plt.pie(
    fruit_sizes,
    labels=fruits,
    explode=(0.1, 0, 0, 0)
)
plt.title("Fruit Sales Distribution")
plt.show()

languages = ["Python", "Java", "C", "JavaScript"]
language_sizes = [45, 25, 20, 10]

plt.pie(
    language_sizes,
    labels=languages,
    explode=(0.1, 0, 0, 0)
)
plt.title("Programming Language Preferences")
plt.show()

#histogram
numbers1 = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7]

plt.hist(numbers1, bins=5, color="skyblue")
plt.title("Frequency Distribution")
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.show()

numbers2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

plt.hist(numbers2, bins=4, color="pink")
plt.title("Data Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()


#3d plot
fig = plt.figure()
axis = plt.axes(projection="3d")

z_values = np.linspace(0, 2, 100)
x_values = z_values * np.sin(20 * z_values)
y_values = z_values * np.cos(20 * z_values)

axis.plot3D(x_values, y_values, z_values, color="blue")
axis.set_title("3D Spiral Plot")
axis.set_xlabel("X Axis")
axis.set_ylabel("Y Axis")
axis.set_zlabel("Z Axis")

plt.show()

#subplot
x5 = [1, 2, 3, 4, 5]
y5 = [4, 7, 9, 13, 18]

x6 = [1, 2, 3, 4, 5]
y6 = [3, 9, 15, 21, 27]

plt.figure(figsize=())

plt.subplot(2, 1, 1)
plt.plot(x5, y5, color="green", linestyle="--")
plt.title("First Line Chart")

plt.subplot(2, 1, 2)
plt.plot(x6, y6, color="red", linestyle="-")
plt.title("Second Line Chart")

plt.show()

fig = plt.figure(figsize=())

x7 = [1, 2, 3, 4, 5]
y7 = [6, 10, 8, 14, 12]

plt.subplot(1, 2, 1)
plt.bar(x7, y7, color="gold")
plt.title("Product Comparison")
plt.xlabel("Products")
plt.ylabel("Values")

subjects = ["Python", "Java", "C", "SQL"]
subject_sizes = [30, 25, 20, 25]

plt.subplot(1, 2, 2)
plt.pie(
    subject_sizes,
    labels=subjects,
    explode=(0, 0, 0, 0.1)
)
plt.title("Subject Distribution")

plt.show()
