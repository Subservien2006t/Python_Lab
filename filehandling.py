# Q1

file1 = open("student_details.txt", "w")

student_name = input("Enter name: ")
roll_number = input("Enter roll no: ")
student_branch = input("Enter branch: ")
semester = input("Enter semester: ")

file1.write(student_name)
file1.write(roll_number)
file1.write(student_branch)
file1.write(semester)

file1.close()


# Q2

file2 = open("student_details.txt", "r")

student_content = file2.readlines()

print(student_content)

file2.close()


# Q3

with open("student_details.txt", "a") as file3:

    student_name = input("Enter name: ")
    roll_number = input("Enter roll no: ")
    student_branch = input("Enter branch: ")
    semester = input("Enter semester: ")

    file3.write(student_name)
    file3.write(roll_number)
    file3.write(student_branch)
    file3.write(semester)


# Q4

with open("sample.txt") as file4:

    file_content = file4.readlines()

    print(file_content)


# Q5

with open("sample.txt") as file5:

    line_content = file5.readlines()

    line_count = 0

    for line in line_content:
        line_count += 1

    print("Count of lines =", line_count)


# Q6

with open("sample.txt") as file7:

    word_count = 0

    for line in file7.readlines():

        words = line.split()

        for word in words:
            word_count += 1

    print("Count of words =", word_count)


# Q7

with open("sample.txt") as file8:

    character_count = 0

    for character in file8.read():
        character_count += 1

    print("Count of characters =", character_count)


# Q9

with open("sample.txt") as file6:

    vowel_count = 0
    consonant_count = 0

    for character in file6.read():

        if character.lower() in "aeiou":
            vowel_count += 1

        elif character.isalpha():
            consonant_count += 1

    print("Vowel count =", vowel_count)
    print("Consonant count =", consonant_count)


# Q16

file9 = open("sample.txt")

file_content = file9.read()

file10 = open("uppercase.txt", "w")

file10.write(file_content.upper())

file9.close()
file10.close()


# Q17

file11 = open("student_records.txt", "w+")

file11.write("Rollno, Name, Marks\n")
file11.write("201, Arjun, 85\n")
file11.write("202, Sneha, 92\n")
file11.write("203, Karan, 78\n")

file11.seek(0)

student_records = file11.readlines()

print(student_records)

file11.close()