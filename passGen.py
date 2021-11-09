import secrets
import string

def shortLowerPass ():
    alphabet = string.ascii_lowercase
    password = ''.join(secrets.choice(alphabet) for i in range(8))

    return password

def shortUpperPass ():
    alphabet = string.ascii_uppercase
    password = ''.join(secrets.choice(alphabet) for i in range(8))

    return password

def shortMixedPass ():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))

    return password

def longMixedPass ():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(16))

    return password

def longLowerPass ():
    alphabet = string.ascii_lowercase
    password = ''.join(secrets.choice(alphabet) for i in range(16))

    return password

def longUpperPass ():
    alphabet = string.ascii_uppercase
    password = ''.join(secrets.choice(alphabet) for i in range(16))

    return password


def customPassword():
    length = int(input("Enter your desired password length: "))
    numbers = input("Do you want your password to contain numbers? Enter yes or no. : ")    
    symbols = input("Do you want your password to contain symbols? Enter yes or no. : ")
   

    if numbers == 'yes' and symbols == 'yes':
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        return password

    elif numbers == 'no' and symbols == 'yes':
        alphabet = string.ascii_letters + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        return password
    
    elif numbers == 'yes' and symbols == 'no':
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        return password
    
    elif numbers == 'no' and symbols == 'no':
        alphabet = string.ascii_letters
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        return password


print("Python Password Generator")
print("-----------------------------")

print("What kind of password would you like to generate?")
print("Options: 1)Short Lower-Case Only, 2)Long Lower-Case Only, 3)Short Upper-Case, 4)Long Upper-Case, 5)Short Mixed, 6)Long Mixed, or 7)Custom.")
print("----------------------------------------------------------------")
print("Short options are 8 characters long, Long are 16 characters long, and for Custom you define length, if numbers are present, and if symbols are present.")

userInput = int(input("Please enter your option: "))
password = ''

if userInput == 1:
    print("Here is your password: ")
    password = shortLowerPass()
    print(password)

elif userInput == 2:
    print("Here is your password: ")
    password = longLowerPass()
    print(password)

elif userInput == 3:
    print("Here is your password: ")
    password = shortUpperPass()
    print(password)

elif userInput == 4:
    print("Here is your password: ")
    password = longUpperPass()
    print(password)

elif userInput == 5:
    print("Here is your password: ")
    password = shortMixedPass()
    print(password)

elif userInput == 6:
    print("Here is your password: ")
    password = longMixedPass()
    print(password)

elif userInput == 7:
    password = customPassword()
    print("Here is your password: ")
    print(password)


print("Do you wish to store your pass word into a text file? Enter yes or no.")
fileSave = (input("Enter your option here: "))

filename = (input("What do you wish to name this file? Please include file extension in name. "))

passwordFile = open(filename, "w")

passwordFile.write(password)






