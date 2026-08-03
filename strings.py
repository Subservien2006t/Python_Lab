#Q1
string1 = input("Enter a string: ")
count = 0
for ch in string1:
    count += 1
print("Length of the string is:", count)

#Q2
string2 = input("Enter a string: ")
cntvowels = 0
cntconsonants = 0
cntdigits = 0
cntspaces = 0
cntothers = 0
for ch in string2:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            cntvowels += 1
        else:
            cntconsonants += 1
    elif ch.isdigit():
        cntdigits += 1
    elif ch.isspace():
        cntspaces += 1
    else:
        cntothers += 1
print("Number of vowels:", cntvowels)
print("Number of consonants:", cntconsonants)
print("Number of digits:", cntdigits)
print("Number of spaces:", cntspaces)
print("Number of other characters:", cntothers)

#Q3
string3 = input("Enter a string: ")
print("Reversed string is:", string3[::-1])

#Q4
string4 = input("Enter a string: ")
reverse = ""
for ch in string4:
    reverse = ch + reverse
if string4 == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
#Q5
string5 = input("Enter a string: ")
cntupper = 0
cntlower = 0
for ch in string5:
    if ch.isupper():
        cntupper += 1
    elif ch.islower():
        cntlower += 1
print("Number of uppercase letters:", cntupper)
print("Number of lowercase letters:", cntlower)

#Q6
string6 = input("Enter a string: ")
old_char = input("Enter the character to be replaced: ")
new_char = input("Enter the new character: ")
string6 = string6.replace(old_char, new_char)

#Q7
string7 = input("Enter a string: ")
string7 = string7.strip()
print("String after removing whitespaces:", string7)

#Q8
string8 = input("Enter a string: ")
char_to_count = input("Enter the character to count: ")
cntchar = 0
for ch in string8:
    if ch == char_to_count:
        cntchar += 1
print("Number of occurrences of ", char_to_count, ":", cntchar)

#Q9
string9 = input("Enter a string: ")
print("First Character:", string9[0])
print("Last Character:", string9[-1])

#Q11
string11 = input("Enter a sentence: ")
count = 0
in_word = False
for ch in string11:
    if ch != ' ' and in_word == False:
        count += 1
        in_word = True
    elif ch == ' ':
        in_word = False
print("Total number of words:", count)

#Q14
string14 = input("Enter a string: ")
print("String in title case:", string14.title())#Q14

 #Q19
string19 = input("Enter a string: ")
substring = input("Enter the substring: ")
if substring in string19:
    print("Substring found.")
else:
    print("Substring not found.")

    #Q20
string20 = input("Enter a sentence: ")
search = input("Enter the word to search: ")
words = string20.split()
count = 0
for word in words:
    if word == search:
        count += 1
print("Occurrences =", count)