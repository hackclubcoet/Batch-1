answer=input("would you like to play? yes/no")

if answer.lower().strip()=="yes":

    answer=input("you  the treasure island, would you like to go left or right?").lower().strip()
    if answer=="left":
        answer=input("you encounter a river, would you like to wait or swim.")

        if answer=="wait":
            print(" you come across three doors, Blue, Red, and Yellow.")

            if answer=="blue":
                print("Eaten by beasts, GAME OVER")

            elif answer=="yellow":
                print("You win! congragulations")

            else :
                print("Burned by fire, GAME OVER")  
        else:
            print("Attacked by trout, GAME OVER")
    else:
        prin("fall into a hole, GAME OVER")
else:
    print("that's too bad")