print("Hello World")

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


print("There was a dude named " + character_name + " who didn't like his name.")

character_name = "Gary"

print("There was a dude named " + character_name + "\n who \"didn't\" like \\ his \ name.")

# print("His age is " + age_num + " years old.")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")
