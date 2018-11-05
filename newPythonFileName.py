
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
print(list_of_peeps)
listOfNums.reverse()
print(listOfNums)


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
