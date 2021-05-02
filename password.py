import string
import random
import time
# random module generates pseudo-random numbers
# time is just for fun

while True:
    password_length = int(input("Enter password length between 8 and 24 characters:"))
    # a prompt and input asking the user to pick
    characters = string.ascii_letters + string.digits + string.punctuation
    # string module constants put together for possible chars in a password string

    if password_length not in range(8,25):
        # password set to 25 in range = up to 24 in output
        print("\nPlease enter a number between 8 and 24.\n")
        time.sleep(.25)
        # checks for required length and waits to make next message more obvious

    else:
        password = []
        # empty password, but defined as variable
        for x in range(password_length):
                password.append(random.choice(characters))
        print(''.join(password))
        # checks for required length and creates password
        time.sleep(.25)
         # waits to make next message more obvious

    if password_length not in range(8,25):
        # checks again for length and if WRONG prompts a message, returns to previous
        new_password = input("Try Again? (y/n): ")
        if new_password.lower() != "y":
            break
    else:
        new_password = input("Make another password? (y/n): ")
         # checks again for length, if RIGHT prompts a final message and restarts
        if new_password.lower() != "y":
            break