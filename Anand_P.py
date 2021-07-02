#Import random module
#Anand P,Batch no:1,Dice Rolling
from random import randint
def rollDice():
#function that returns number between [1,6]
    return randint(1,6)
#define variables total and i
total = 0
i=0
#while loop to roll again if total less than 50
while total < 50:
    new_roll = rollDice()
    total += new_roll
    #if condition to find total less than 50
    if total<50:
        i+=1
        print('You rolled a {}. The new total is {}'.format(new_roll, total))
print("you rolled dice ",i,"times")