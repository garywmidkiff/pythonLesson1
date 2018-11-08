# Deliberate use of poor coding style is often done intentionally to learn what Python can and cannot handle for syntax.  Test.

from StudentFile import StudentClass

student1 = StudentClass("Jim", "Business", 3.1, False)

print(student1.major)

exit()














# Modules and Pip




# writing to files
employee_file = open("employees.txt", "w") # w for write, a for append, r+ for read and write
employee_file.write("Toby - Human Resources")
employee_file.close()
exit()









# reading from files
employee_file = open("employees.txt", "r") # w for write, a for append, r+ for read and write

print(employee_file.readable())
# print(employee_file.readlines()[4])
# listoflines = employee_file.readlines()
# print(listoflines[3])
print(employee_file.readlines())
# print(employee_file.read())
# print(employee_file.readline())

employee_file.close()



employee_file = open("employees.txt", "r") # w for write, a for append, r+ for read and write
print(employee_file.readable())
for line in employee_file.readlines():
    print(line)

employee_file.close()


exit()



# try/except
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("ZeroDivisionError exception was thrown and caught")
    print(err)
except ValueError as err:
    print("ValueError exception was thrown and caught")
    print(err)

exit()

'''
How to
do mulit-line
comments
'''
# translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        # if letter in "AEIOUaeiou":
        if letter.lower() in "aeiou":
            if letter.isupper(): # <---  doesn't change the value stored in letter, merely returns the upper...
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))

exit()




# 2D lists and nested loops
numberGrid = [
    [0, 1, 2, 3],
    [4,5,6],
    [7,8,9],
    [10]
]
print(numberGrid[0][1])

# Let's print all the values - the stoopid way
for slowIndex in range(len(numberGrid)):
    for fastIndex in range(len(numberGrid[slowIndex])):
        print(numberGrid[slowIndex][fastIndex])

# a cooler way
for row in numberGrid:
    for col in row:
        print(col)

exit()


print(pow(2,3))
print(2**-3)

exit()



friends = ["Jim", "John", "Karen", "Jason", "Joe"]
for index in range(len(friends)): # len returns 5 conveniently considering how range is working, non-inclusive of the
                                  # last element from what I had expected to happen.
    print(friends[index])

exit()

for index in range(3, 10): # prints from 3-9
    print(index)

for index in range(10): # prints from 0-9
    print(index)

exit()




# Tuples are immutable.
coordinates = (4, 5) # use [] for lists, () for tuples.  Use tuples for data that's not going to change.
other_coordinates = (4, 5, 6, 7, 8) # use [] for lists, () for tuples.  Use tuples for data that's not going to change.
print(other_coordinates[2])

# here's a list of tuples:
listOfTuples = [(4,5), (6,7), (80,34)]
print(listOfTuples[2])
print(listOfTuples[2][1])

exit()





for letter in "Giraffe Academy":
    print(letter)



exit()

i = 1
while i <= 10:
    print(i)
    i += 1

print ("done with loop")


exit()




# Dictionaries use curly braces
monthConversions = {
    "Jan" : "January",
    "Feb": "February",
    "Mar": "March",
}

print(monthConversions["Mar"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Apr"))
print(monthConversions.get("Apr", "Not a valid key"))


exit()



# skipping this next experiment....  too basic, like much of this course.
num1 = float(input("Enter first number: "))
op = (input("Enter operator: "))
num2 = float(input("Enter second number: "))

# if op == "+":










def maxnum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

if ("dog" == "dog"):
    print("eval'd to true")


print(maxnum(3,40,5))
exit()


# Functions
def FuncName(name, age, age_num):
    # must be indented
    print("hello " + name + " you are " + age + " or said otherwise, " + str(age_num))

FuncName("Mike", "70", 3)


def cube(num):
    return num*num*num

print(cube(3))

result = cube(4)
print(result)


isMale = False
isTall = True

if isMale or isTall:
    print("am male or tall")
    print("I said u r male or tall.")
else:
    print("not male")

if isMale and isTall:
    print("male and tall")
elif isMale and not(isTall):
    print("short male")
elif not(isMale) and isTall:
    print("tall female")
else:
    print("both false")



exit()









# Tuples are immutable.
coordinates = (4, 5) # use [] for lists, () for tuples.  Use tuples for data that's not going to change.
print(coordinates[0])

# here's a list of tuples:
listOfTuples = [(4,5), (6,7), (80,34)]


exit()








# lists....
list_of_peeps = ["ads", "joe", "dave", "john", "blah Blah Sr."]
# strings, numbers, boolean
mixed_list = ["string", 2.7, False]
print(list_of_peeps)
print(mixed_list)
print(mixed_list[2])
print(list_of_peeps[-1])
print(mixed_list[1:])
print(list_of_peeps[1:3])
list_of_peeps[0] = "ASDF"
print(list_of_peeps[0])
list_of_peeps.extend(mixed_list)
print(list_of_peeps)
list_of_peeps.append("additional item at end of list")
list_of_peeps.insert(1, "jason")
print(list_of_peeps)
list_of_peeps.remove(False)
print(list_of_peeps)
list_of_peeps.pop()
print(list_of_peeps)
print(list_of_peeps.index("dave"))
print(list_of_peeps.count(2.7))

listOfNums = [6,4,34,22,1,0]
print(listOfNums)
listOfNums.sort()
print(listOfNums)
listOfNums.reverse()
print(listOfNums)
SecondListOfNums = listOfNums.copy()
print(SecondListOfNums)



list_of_peeps.clear()
print(list_of_peeps)
exit()


num1 = input("enter a number:")
num2 = input("enter another number: ")
result = float(num1) + float(num2)
print(result)
exit()



name = input("prompt for name goes here: ")
age = input("prompt for age goes here: ")
print("name entered was: " + name + "!  and age is: " + age)
exit()




print("Hello World")

print(-2.0987)
print(3+4.5)
print (3*4.5)
print(3/4.5)
print(10%3)

mynum=5
print(mynum)
print(str(mynum)+" is a great number.")
numx = -5.7
print(abs(numx))
print(pow(3,4))
print(max(4,6))
print(min(4,6))
print(round(3.7))

from math import *
print("floor:")
print(floor(3.7))
print("ceil:")
print(ceil(3.2))
print("square root:")
print(sqrt(36))



exit()







character_name: str = "John"
mixed_capitalization_string = "This Is A Slow Process."
character_age = "35"
age_num = 36.1234567
bool_val = True
other_bool_val = False

print(mixed_capitalization_string)
print(mixed_capitalization_string.lower())
print(mixed_capitalization_string.upper())

print(mixed_capitalization_string.isupper())
print(mixed_capitalization_string.upper().isupper())

print(len(mixed_capitalization_string))
print(mixed_capitalization_string[22])
print(mixed_capitalization_string.index("is"))
print(mixed_capitalization_string.replace("is", "Has Been")) # gotcha
print(mixed_capitalization_string.replace("Is", "Has Been"))
print(mixed_capitalization_string.replace("non-existent", "Has Been"))


print("There was a dude named " + character_name + " who didn't like his name.")

character_name = "Gary"

print("There was a dude named " + character_name + "\n who \"didn't\" like \\ his \ name.")

# print("His age is " + age_num + " years old.")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")
