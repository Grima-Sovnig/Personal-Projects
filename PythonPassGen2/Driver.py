from Generator import Generator
from Encryptor import Encryptor
import os

generator = Generator() #Creation of a Generator Object to create the passwords the user desires.
encryptor = Encryptor() #Creation of a Encryptor Object to encrypt and decrypt files if the user wants to save the file.
#Printing of main menu for the user to make their selection.
print("Welcome to the Python Password Generator")
print("-------------------------------------------------------------------------")

print("What kind of password would you like to create today?")
print("Here is a list of possible options:")
print("-------------------------------------------------------------------------")
print("Option 1: Short Lower-Case Only") 
print("Option 2: Long Lower-Case Only")
print("Option 3: Short Upper-Case Only")
print("Option 4: Long Upper-Case Only")
print("Option 5: Short Mixed")
print("Option 6: Long Mixed") 
print("Option 7: Custom Generator")
print("Option 8: Load Encrypted File")

print("Short options contain 8 characters, while Long options are 16 characters.")
print("Custom allows for full control of length and content.")
print("Option 8 is for those who have ran the program previously.")
print("-------------------------------------------------------------------------")
#Taking in user input and returning the password based on their decision.
userInput = int(input("Please enter your option: "))
#Variable Creation
password = ''
keyFile = ''
loadedKey = ''
encryptedFileName = ''
decryptedFileName = ''
userSave = ''
tempFileName = 'temp.txt'

if userInput == 1:
    print("Here is your password: ")
    password = generator.shortLowerPass()
    print(password)

elif userInput == 2:
    print("Here is your password: ")
    password = generator.longLowerPass()
    print(password)

elif userInput == 3:
    print("Here is your password: ")
    password = generator.shortUpperPass()
    print(password)

elif userInput == 4:
    print("Here is your password: ")
    password = generator.longUpperPass()
    print(password)

elif userInput == 5:
    print("Here is your password: ")
    password = generator.shortMixedPass()
    print(password)

elif userInput == 6:
    print("Here is your password: ")
    password = generator.longMixedPass()
    print(password)

elif userInput == 7:
    password = generator.customPassword()
    print("Here is your password: ")
    print(password)
    
elif userInput == 8:
    print("Welcome back, there are a few steps before we begin decryption.")
    print("You will need to make sure you key file has been moved to the directory.")
    keyFile = (input("Please enter the name of the key file with the .key ext: "))
    loadedKey = encryptor.key_load(keyFile)
    print(loadedKey)
    
    encryptedFileName = (input("Please enter the name of the encrypted file: "))
    decryptedFileName = (input("Enter the name you wish for the decrypted file: "))
    encryptor.file_decrypt(loadedKey,encryptedFileName,decryptedFileName)
    print("Your password should now be stored into the desired decrypted filename.")
    
    
    
print("-------------------------------------------------------------------------")

print("Do you wish to save your password to a encrypted file?")
fileSave = (input("Yes or No?: "))

if fileSave == 'Yes':
    tempFile = open(tempFileName, 'w')
    tempFile.write(password)
    loadedKey = encryptor.key_creation()
    keyFile = (input("Enter the desired name for the key file: "))
    encryptor.key_write(loadedKey, keyFile)
    print("The key has been written to the desired file.")
    encryptedFileName = (input("Please enter the desired name for the encrypted file: "))
    encryptor.file_encrypt(loadedKey, tempFileName, encryptedFileName)
    print("Your password should be encrypted in the desired file.")
    
    print("Performing Final Cleanup before exiting program.")
    
    if os.path.exists(tempFileName):
        os.remove(tempFileName)

else:
    print("Thank you for using this password generator.")
    
