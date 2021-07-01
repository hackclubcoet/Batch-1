a = []


# Adhish_Aravind-1-ToDoList

# function for adding activities into the list
def adding():
    activity = input("enter the activity:")
    a.append(activity)
    print(activity)


# function for displaying the list
def display():
    print("To-Do List:", end="\n")
    print('\n'.join([str(i) for i in a]))


# while loop for entering choice
while True:
    ch = input("Do you want to add anything(y/n):")  # prompts user for a choice(y/n)
    if ch == "y" or ch == "Y":
        adding()
    elif ch == "n" or ch == "N":
        display()
        break
    else:
        print("Invalid Option")
