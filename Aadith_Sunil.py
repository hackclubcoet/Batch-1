from random import choice #importing choicefunction from random module
#AadithSunil-1-StonePaperScissors

def stonepaperscissors(name=input("Enter your name : ").capitalize(),gamelaw={"stone":"paper","paper":"scissors","scissors":"stone"}): #defining a function 
    guess=input("{} >> ".format(name)).lower() #user guessing
    if guess=="exit":  #stoping condition for recursion (user enter "exit" ro exit the game)
        print()
    elif guess in list(gamelaw.keys()): 
        machineguess=choice(list(gamelaw.keys()))
        print("Machine >> ",machineguess.capitalize())
        if machineguess==guess:        #machine and user opting for same will be a draw
            print("Its a Draw...")
        elif gamelaw[machineguess]==guess:       #The dictionary gamelaw is predefined in such a way that the key can be defeated by the value
            print(name," wins...")
        elif gamelaw[guess]==machineguess:
            print("Machine wins...")
        return stonepaperscissors(name)
    else:   #try again for unexpected inputs
        print("Unexpected input...try again...")
        return stonepaperscissors(name)

print("\tStone, Paper, Scissors")
print("")
stonepaperscissors() 


