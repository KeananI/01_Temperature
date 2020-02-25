import re

data = ['I', 'Love', 'computers']

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a Filename (Leave off the extension): ")

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"
        else:
            problem = ("(no {}'s allowed)".format(letter))
        has_error = "yes"

    if filename == "":
        problem = "Can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
    else:
        print("You entered a valid filename")