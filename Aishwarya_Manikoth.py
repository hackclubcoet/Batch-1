#pythonproject
# Aishwarya Manikoth-1-Currency converter(Dollar to Rupees and vice versa)

def multiply(a, b):
    return a*b
def division(a, b):
    return a/b
# programme starts here
print("To convert:\nFrom Dollar to Rupees--enter 1\nFrom Rupees to Dollar--enter 2\n")
a = input()  # TO FIND  WHAT THE USER WANTS TO CONVERT
if a == "1":  # TO CONVERT DOLLAR TO RUPEES
    dollar = float(input("enter the amount in Dollar\n"))  # PROMPTS  THE USER FOR THE AMOUNT IN DOLLAR
    rupees = multiply(dollar, 74.28)
    # Rupees = Dollar * 74.28
    print("$ %0.2f " % dollar, " = %0.2f" % rupees, "rs")  # OUTPUT AMOUNT TO USER
    print("**************************")
elif a == "2":  # TO COVERT RUPEES TO DOLLAR1
    rupees = float(input("enter the amount in Rupees\n"))  # PROMPTS  THE USER FOR THE AMOUNT IN DOLLAR
    dollar = division(rupees, 74.28)
    # Dollar = Rupees / 74.28
    print("% 0.2f" % rupees, "rs", " = ", "$ % 0.2f" % dollar)  # OUTPUT AMOUNT TO USER
    print("**************************")
else:  # IF USER ENTERED SOMETHING ELSE
    print("**************************")
    print("Invalid input , Try Again")
    print("**************************")
