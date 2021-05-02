import string
import random
import time

# * key means all, so in this case all from the random module
# random module generates pseudo-random numbers, built-in to python
while True:
    password_length = int(input("Enter password length between 8 and 24 characters:"))
    # A prompt and input asking the user to pick
    characters = string.ascii_letters + string.digits + string.punctuation
    # string module constants put together for possible chars in a password string

    if password_length not in range(8,25):
        print("\nPlease enter a number between 8 and 24.\n")
        time.sleep(.25)

    else:
        password = []
        # empty password, but defined as variable
        for x in range(password_length):
                password.append(random.choice(characters))

        print(''.join(password))
        time.sleep(.25)

    if password_length not in range(8,25):    
        new_password = input("Try Again? (y/n): ")
        if new_password.lower() != "y":
            break
    else:
        new_password = input("Make another password? (y/n): ")
        if new_password.lower() != "y":
            break