# unique_id : Abdul Anzil B - Batch 1 - Calculator

""" This is a simple console based calculator for the addition, subtraction, multiplication, division,
 sine and cosine operations """

# to import the module math
import math


def find_sum(a, b):
    '''This function returns the sum of given two numbers'''
    return a + b


def find_dif(a, b):
    '''This function returns the difference of given two numbers'''
    return a - b


def find_product(a, b):
    '''This function returns the product of given two numbers'''
    return a * b


def find_division(a, b):
    '''This function returns the division of given two numbers'''
    return a / b


def find_sine(angle):
    '''This function returns the value of sine of given angle'''
    return math.sin(math.radians(angle))


def find_cosine(angle):
    '''This function returns the value of cosine of given angle'''
    return math.cos(math.radians(angle))


answer = 'y'
# the below while loop is done for whether the user need to do the calculation again or end the program
# it is asked at the end of the program

while answer == "y":

    print("Select the operation you need by entering \n\t"
          "* 1 for Addition, \n\t"
          "* 2 for Subtraction, \n\t"
          "* 3 for Multiplication, \n\t"
          "* 4 for Division, \n\t"
          "* 5 for Sine operation, \n\t"
          "* 6 for Cosine operation.")

    while True:
        '''we use try and except to avoid possible user input errors'''
        try:
            choice = int(input("Enter your choice : "))
            # variable choice stores the operation we needed
            if choice in range(1, 7):
                break
            else:
                print("Invalid option!!", end=" ")
                continue
        except ValueError:
            print("Invalid option!!", end=" ")

    # for taking values from user

    if choice in range(1, 5):
        while True:
            '''to take the first number without any input error'''
            try:
                first_num = float(input("Enter first number : "))
                break
            except ValueError:
                print("Invalid input!!", end=" ")

        while True:
            '''to take the second number without any input error'''
            try:
                second_num = float(input("Enter second number : "))
                if choice == 4 and second_num == 0:
                    '''to avoid error of division by Zero'''
                    print("Can't divide by Zero!!", end=" ")
                    continue
                break
            except ValueError:
                print("Invalid input!!", end=" ")
    else:
        while True:
            '''to take the value of angle without any input error'''
            try:
                angle = float(input("Enter the angle in degree : "))
                break
            except ValueError:
                print("Invalid input!!", end=" ")

    # Calculations by calling particular fuctions

    if choice == 1:
        print(str(first_num) + " + " + str(second_num) + " = " + str(find_sum(first_num, second_num)) + " .")
    elif choice == 2:
        print(str(first_num) + " - " + str(second_num) + " = " + str(find_dif(first_num, second_num)) + " .")
    elif choice == 3:
        print(str(first_num) + " * " + str(second_num) + " = " + str(find_product(first_num, second_num)) + " .")
    elif choice == 4:
        print(str(first_num) + " / " + str(second_num) + " = " + str(find_division(first_num, second_num)) + " .")
    elif choice == 5:
        print("sin(" + str(angle) + ") = " + str("{:f}".format(find_sine(angle))) + " .")
        # "{:f}".format() converts the scientific notation of answer to decimal notation
    else:
        print("cos(" + str(angle) + ") = " + str("{:f}".format(find_cosine(angle))) + " .")

    # variable answer is for YES/NO from user, whether to do calculation again or not
    answer = input("Enter 'y' to do the calculation again or \n"
                   "Enter 'n' to end the program : ")
    while answer != 'y' and answer != 'n':
        answer = input("Invalid answer!! Enter 'y' or 'n' : ")
