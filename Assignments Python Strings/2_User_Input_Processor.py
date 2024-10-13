# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.
while True:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    # Check if both first_name and last_name are at least 2 characters long
    if len(first_name) >= 2 and len(last_name) >= 2:
        print("Name is valid.")
        break  # Exit the loop if the name is valid
    else:
        print("Name is invalid. Both first and last names must be at least 2 characters long.")
