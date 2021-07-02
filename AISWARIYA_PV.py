#shopping cart
#Aiswariya_pv-batch1-shopping_cart
#Appending the user's choice to the shopping and allow user to add, remove and continue displaying the cart until the user wishes to exist.

user_input = ''

items = ["Apple", "carrots", "mangos", "pineapples", "Grapes"]
print("Default List is")
print(*items, sep="\n")


def my_list():
    print("Select a option to add or remove from List")
    print("Type a to add an item")
    print("Type d to delete an item")
    print("Type c to exit")


while user_input != 'c':
    my_list()
    user_input = input("Type the function to execute ")

    if user_input == 'a':
        item = input("Enter the name of the item to add in the List ")
        items.append(item)
        print("New List added = " + str(items))

    elif user_input == 'd':
        item = input("Enter the item name to delete from the List ")
        items.remove(item)
        print("Successfully removed " + str(items))
    elif user_input == 'c':
        print("Bye....")
    else:
        print("Invalid operation")