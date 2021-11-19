import secrets
import string

class Generator():

    def shortLowerPass(self):
        alphabet = string.ascii_lowercase
        password = ''.join(secrets.choice(alphabet) for i in range(8))

        return password

    def shortUpperPass(self):
        alphabet = string.ascii_uppercase
        password = ''.join(secrets.choice(alphabet) for i in range(8))

        return password

    def shortMixedPass(self):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))

        return password

    def longMixedPass(self):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(16))

        return password

    def longLowerPass(self):
        alphabet = string.ascii_lowercase
        password = ''.join(secrets.choice(alphabet) for i in range(16))

        return password

    def longUpperPass(self):
        alphabet = string.ascii_uppercase
        password = ''.join(secrets.choice(alphabet) for i in range(16))

        return password


    def customPassword(self):
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
