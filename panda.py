
import pandas as pd
#Q1
students = {
    "Student_ID": [201, 202, 203, 204, 205],
    "Name": ["Arjun", "Meera", "Kavya", "Vikram", "Anaya"],
    "Python": [78, 88, 67, 92, 81],
    "DBMS": [82, 79, 72, 85, 86],
    "Mathematics": [75, 91, 69, 89, 84]
}

table = pd.DataFrame(students)

table["Total"] = table["Python"] + table["DBMS"] + table["Mathematics"]
table["Average"] = table[["Python", "DBMS", "Mathematics"]].mean(axis=1)

print("\n========== Q1: STUDENT MARKS ==========")
print(table)

print("\nStudents with average above 75:")
print(table[table["Average"] > 75])

#Q2
employees = {
    "Employee_ID": [11, 12, 13, 14, 15],
    "Name": ["Riya", "Aditya", "Sneha", "Varun", "Ishita"],
    "Department": ["IT", "CSE", "HR", "Finance", "CSE"],
    "Salary": [48000, 72000, 58000, 85000, 42000],
    "Experience": [3, 6, 4, 9, 2]
}

emp_df = pd.DataFrame(employees)

print("\n========== Q2: EMPLOYEE ANALYSIS ==========")
print("Employees earning above 50000:")
print(emp_df[emp_df["Salary"] > 50000])

print("\nAverage Salary:", emp_df["Salary"].mean())
print("Highest Salary:", emp_df["Salary"].max())

print("\nEmployee with highest experience:")
print(emp_df.loc[emp_df["Experience"].idxmax()])

#Q5
orders = {
    "Order_ID": [301, 302, 303, 304, 305],
    "Customer": ["Aarav", "Diya", "Kabir", "Ira", "Vivaan"],
    "Product": ["Tablet", "Laptop", "Mouse", "Speaker", "Printer"],
    "Quantity": [2, 1, 4, 3, 2],
    "Price": [15000, 55000, 700, 2500, 9000],
    "Discount": [1000, 4000, 200, 500, 800]
}

order_df = pd.DataFrame(orders)

order_df["Final_Amount"] = (
    order_df["Quantity"] * order_df["Price"] - order_df["Discount"]
)

print("\n========== Q5: ORDER ANALYSIS ==========")
print("All Orders:")
print(order_df)

print("\nOrders above 5000:")
print(order_df[order_df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(order_df.loc[order_df["Final_Amount"].idxmax()])

print("\nAverage Order Value:", order_df["Final_Amount"].mean())

#Q6
attendance_data = {
    "Student_ID": [211, 212, 213, 214, 215],
    "Name": ["Dev", "Tara", "Om", "Nisha", "Yash"],
    "Department": ["CSE", "IT", "ENTC", "CSE", "IT"],
    "Total_Classes": [120, 100, 150, 100, 80],
    "Classes_Attended": [100, 68, 105, 72, 60]
}

attendance_df = pd.DataFrame(attendance_data)

attendance_df["Attendance_Percentage"] = (
    attendance_df["Classes_Attended"]
    / attendance_df["Total_Classes"]
) * 100

print("\n========== Q6: ATTENDANCE ANALYSIS ==========")
print(attendance_df)

print("\nStudents with attendance below 75%:")
print(attendance_df[attendance_df["Attendance_Percentage"] < 75])

#Q8
marks_data = {
    "Aniket": 82,
    "Sakshi": 94,
    "Pranav": 68,
    "Mitali": 76,
    "Atharva": 89
}

marks_series = pd.Series(marks_data)

print("\n========== Q8: STUDENT SERIES ==========")
print("Student Marks:")
print(marks_series)

print("\nMarks of Sakshi:", marks_series["Sakshi"])
print("Maximum Marks:", marks_series.max())
print("Minimum Marks:", marks_series.min())
print("Average Marks:", marks_series.mean())

print("\nStudents scoring above 75:")
print(marks_series[marks_series > 75])

#Q10
patient_ages = {
    501: 52,
    502: 67,
    503: 81,
    504: 39,
    505: 59
}

age_series = pd.Series(patient_ages)

print("\n========== Q10: PATIENT AGE ANALYSIS ==========")
print("Average Age:", age_series.mean())

print("\nOldest Patient ID:", age_series.idxmax())
print("Oldest Patient Age:", age_series.max())

print("\nYoungest Patient ID:", age_series.idxmin())
print("Youngest Patient Age:", age_series.min())

print("\nPatients above 60 years:")
print(age_series[age_series > 60])

#Q12
csv_data = {
    "Student_ID": [201, 202, 203, 204, 205, 206],
    "Name": ["Arjun", "Meera", "Kavya", "Vikram", "Anaya", "Dev"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT", "CSE"],
    "Python": [78, 88, 67, 92, 81, 74],
    "DBMS": [82, 79, 72, 85, 86, 80],
    "Maths": [75, 91, 69, 89, 84, 77]
}

pd.DataFrame(csv_data).to_csv("students.csv", index=False)

student_df = pd.read_csv("students.csv")

print("\n========== Q12: CSV ANALYSIS ==========")
print("First 5 records:")
print(student_df.head())

print("\nLast 5 records:")
print(student_df.tail())

student_df["Total"] = student_df[["Python", "DBMS", "Maths"]].sum(axis=1)
student_df["Average"] = student_df[["Python", "DBMS", "Maths"]].mean(axis=1)

print("\nTotal and Average Marks:")
print(student_df[["Student_ID", "Name", "Total", "Average"]])

print("\nStudents with average above 75:")
print(student_df[student_df["Average"] > 75])

print("\nStudent with highest average:")
print(student_df.loc[student_df["Average"].idxmax()])

print("\nAverage marks of each subject:")
print(student_df[["Python", "DBMS", "Maths"]].mean())

print("\n========== ALL PROGRAMS COMPLETED ==========")
