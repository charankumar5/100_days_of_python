print(type(123))

print(type("123"))

print(type(True))

print(type(32.424))

print(type([1,2,3]))

print(type({"name":"vaishu"}))

print(type({"name:vaishu"}))


#type casting.

string = "123"
print("type casting.")
print(type(string))
print(int(string))
print(bool(string))
print("Number of letters in your name: " + str(len(input("What is your name? "))))