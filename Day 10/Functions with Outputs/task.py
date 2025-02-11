def format_name(first_name, last_name):
    # first_name = input(str("Enter your first name: "))
    # last_name = input(str("Enter your last name: "))
    fullname = first_name+ " "+last_name
    return fullname.title()

formated_name = format_name("charan", "poreddy")
print(formated_name)

