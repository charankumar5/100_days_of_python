programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])
#updated the dictionary value using the existing key.
programming_dictionary["Bug"] = "No error in a program that prevents from running as expected:"
print(programming_dictionary["Bug"])
# The below line wipes the dictionary.
# programming_dictionary = {}
# print(programming_dictionary["Bug"])

# Loop through the dict.
for item in programming_dictionary:
    print(item + ":" + programming_dictionary[item])
