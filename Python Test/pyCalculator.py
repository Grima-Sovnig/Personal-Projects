def addition ():
    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))
    finalAnswer = firstNumber + secondNumber
    return [finalAnswer]

def subtraction ():
    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))
    finalAnswer = firstNumber - secondNumber
    return [finalAnswer]

def multiplication ():
    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))
    finalAnswer = firstNumber * secondNumber
    return [finalAnswer]

def division ():
    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))
    if secondNumber == 0:
        print("Please enter a number other than zero for the second number.")
        secondNumber = float(input("Re-enter your second number here: "))
    
    finalAnswer = firstNumber / secondNumber

    return [finalAnswer]

def average ():
    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))
    finalAnswer = (firstNumber + secondNumber) / 2
    return [finalAnswer]



#Main Body

while True:
    finalAnswer = 0

    print("Welcome to my Python Calculator")
    print("Enter Addition for the Addition Function")
    print("Enter Subtraction for the Subtraction Function")
    print("Enter Multiplication for the Multiplication Function")
    print("Enter Division for the Division Function")
    print("Enter Average for the Average Function")
    print("Type Quit to exit the program")


    userChoice = input("")

    if userChoice != "Quit":
        if userChoice == "Addition":
            finalAnswer = addition()
            print("Answer is ", finalAnswer)
        elif userChoice == "Subtraction":
            finalAnswer = subtraction()
            print("Answer is ", finalAnswer)
        elif userChoice == "Multiplication":
            finalAnswer = multiplication()
            print("Answer is ", finalAnswer)
        elif userChoice == "Division":
            finalAnswer = division()
            print("Answer is ", finalAnswer)
        elif userChoice == "Average":
            finalAnswer = average()
            print("Answer is ", finalAnswer)
        else:
            print("Please enter a valid option.")
    else:
        False
        break