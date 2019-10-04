# Iterative Statements

# Review

"""
Try this guy first:
if expression: Expression must evaluate to a True value
    statement

If the first doesn't work, try the next
elif (else if) expression:
    statement

If all else fails, run this guy
else:
    statement
"""

# While loop

"""
while expresion: Expression must evaluate to a True value
    statement
"""

"""
This runs forever, use CTRL + C to break out of it
while True:
    print("Hello")
"""

a = 0

while a < 3:
    print(a)
    a += 1 # Same thing as a = a + 1

user_input = None
while True:
    user_input = int(input("Enter the number 10: "))
    if user_input == 10:
        break

print("Thank you for inputting the number 10.")

"""
/// Write a program and ask the user to enter a number. The number should be between 1 to 10. If the user enters 
/// a valid number, display "Valid" on the console. Otherwise, display "Invalid". (This logic is used a lot in 
/// applications where values entered into input boxes need to be validated.) If the user enters the word 'exit',
/// we exit
"""

while True:
    user_input = input("Enter a number between 1 and 10 or type 'exit' to exit: ")

    if user_input == 'exit':
        break

    if int(user_input) >= 1 and int(user_input) <= 10:
        print("Valid")
    else:
        print("Invalid")


"""
/// Write a program and ask the user to enter a few words separated by a space. Use the words to 
/// create a variable name with PascalCase convention. For example, if the user types: 
/// "number of students", display "NumberOfStudents". Make sure the program is not dependent on 
/// the casing of the input. So if the input is "NUMBER OF STUDENTS", it should still display 
/// "NumberOfStudents". If the user doesn't supply any words, display "Error".
"""
# The lazy fox jumps over the river.
#TheLazyFoxJumpsOverTheRiver.
words = input("Enter a few words separated by a space: ").split(' ')

i = 0
while i < len(words):
    # word = words[i]
    # new_word = word.lower().capitalize()
    # print(new_word)
    words[i] = words[i].lower().capitalize()
    i += 1

print(''.join(words))

"""
List Comprehension Reveiw
"""

my_list = []
my_list.append("asdba")
my_list.append("some other junk")
my_list.insert(1, "insert me between the junk")
my_list += ["asdfasdfsd"]

my_list[0] = 1234

print(my_list[:2])
print(my_list[2:])

print(my_list[:])
print(my_list)


numbers = [1, 3, 17, 2, 69, 4, 6, 10, 420, 42, 18]

print(numbers)
print(numbers[::-1])
print(numbers[::3])

length = len(numbers)
print(length)

counter = 0
while counter < len(numbers):
    print(numbers[counter])
    # counter = counter + 1
    counter += 1

print('-----------')

counter = len(numbers)
while counter > 0:
    counter -= 1
    print(numbers[counter])

print('-----------')

counter = 0
while counter < len(numbers):
    numbers[counter] = 'ABC'
    print(numbers[counter])
    counter += 1

print(numbers)

numbers = [1, 3, 17, 2, 69, 4, 6, 10, 420, 42, 18]

"""
for some_variable in some_collection:
    do_something...
"""

for number in numbers:
    print(number)

print('-----------')

for number in numbers:
    number = 'ABC'
    print(number)

print(numbers)

numbers = [1, 3, 17, 2, 69, 4, 6, 10, 420, 42, 18]
print(numbers)

for i in range(len(numbers)):
    # [0, 1, 2, ..., 10]
    for j in range(len(numbers)-1, 0, -1):
        if numbers[j-1] < numbers[j]:
            tmp = numbers[j-1]
            numbers[j-1] = numbers[j]
            numbers[j] = tmp
    print(numbers)
print(numbers)


"""
/// Write a program and ask the user to enter a few words separated by a space. Use the words to 
/// create a variable name with PascalCase convention. For example, if the user types: 
/// "number of students", display "NumberOfStudents". Make sure the program is not dependent on 
/// the casing of the input. So if the input is "NUMBER OF STUDENTS", it should still display 
/// "NumberOfStudents". If the user doesn't supply any words, display "Error".
"""
# The lazy fox jumps over the river.
#TheLazyFoxJumpsOverTheRiver.
# words = input("Enter a few words separated by a space: ").split(' ')

# i = 0
# while i < len(words):
#     # word = words[i]
#     # new_word = word.lower().capitalize()
#     # print(new_word)
#     words[i] = words[i].lower().capitalize()
#     i += 1

# print(''.join(words))

# The lazy fox jumps over the river.
#TheLazyFoxJumpsOverTheRiver.

words = input("Enter a few words separated by a space: ").split(' ')
new_list = []
# response = ''
for word in words:
    new_list.append(word.lower().capitalize())

print(''.join(new_list))
  # response+=word.lower().capitalize()    
#print(response)

"""
/// Write a program and ask the user to enter an English word. Count the number of vowels 
/// (a, e, o, u, i) in the word. So, if the user enters "inadequate", the program should display 
/// 6 on the console. Make sure the program calculates the number of vowels irrespective of the 
/// casing of the word (eg "Inadequate", "inadequate" and "INADEQUATE" all include 6 vowels).
"""

word = input("Enter a word here: ")

count = 0

for letter in word:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        if letter == vowel:
            count += 1

print(count)


"""
while expresson:  runs when expression is True
    statement

for number in numbers: Loops through every element of the list or array
    statement

for _ in range(10): This will run 10 times
    statement
"""
