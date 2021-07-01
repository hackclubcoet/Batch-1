#treasure hunt game
#Ameena_Harees-batch1-treasure_hunt
#player must find treasures without getting eaten by the beast or burned by fire.
answer = input("would you like to play? yes/no")
again = "yes"

while again == "yes":
    if answer.lower().strip()=="yes":

        dir_ = input("you ener the treasure island, would you like to go left or right?").lower().strip()
        if dir_ == "left":
            act = input("you encounter a river, would you like to wait or swim.")

            # here the player have to choose swim or wait

            if act == "wait":
                print (" you come across three doors, Blue, Red, and Yellow.")
                door = input("which door would you like to open?")
                if door == "blue":
                    print("Eaten by beasts, GAME OVER")
                elif door == "yellow":
                    print("You win! congratulations")
                elif door == "red":
                    print("Burned by fire, GAME OVER")
                else:
                    print("GAME OVER, Try again")

            else:
                print("Attacked by trout, GAME OVER")


        else:
            print("fall into a hole, GAME OVER")
    else:
        print("that's too bad")

    again = input("try again yes or no")