import string
import random

# Get desired password length from the user
password_length = int(input("Enter the desired password length: "))

# Display character set options
print('''Select the character set to include in the password:
        1. Letters (Uppercase & Lowercase)
        2. Numbers (Digits)
        3. Special characters
        4. Done selecting (Generate password)
''')

# Initialize a variable to hold all selected character types
available_characters = ""

# Loop to select character sets
while True:
    selection = input("Enter your option (1/2/3/4): ")

    if selection == '1':
        available_characters += string.ascii_letters
        print("Letters added to the character set.")

    elif selection == '2':
        available_characters += string.digits
        print("Numbers added to the character set.")

    elif selection == '3':
        available_characters += string.punctuation
        print("Special characters added to the character set.")

    elif selection == '4':
        if available_characters:
            print("Generating your password...")
            break
        else:
            print("No character set selected. Please choose at least one option.")

    else:
        print("Invalid option. Please select a valid number (1/2/3/4).")

# Generate the random password
if available_characters:
    password = ''.join(random.choice(available_characters) for _ in range(password_length))
    print(f"Your randomly generated password is: {password}")
else:
    print("Password generation failed. No valid character set was selected.")
