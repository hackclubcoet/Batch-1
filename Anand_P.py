from random import randint

def rollDice():
    return randint(1,6)

total = 0
while total < 50:
    new_roll = rollDice()
    total += new_roll
    if total<50:
        print('You rolled a {}. The new total is {}'.format(new_roll, total))