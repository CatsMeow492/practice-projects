#You are making a digital menu to order food.
#The menu is stored as a list of items.
#Your program needs to take the index of the item as input and output the item name.
#In case the index is not valid, you should output "Item not found".
#In case the index is valid and the item name is output successfully, you should output "Thanks for your order".

menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']
#your code goes here

order = input()

try:
    order = int(order)
    print(menu[order])
    print("Thanks for your order")
except (ValueError, TypeError):
    print("Item not found")
except:
    print("Item not found")


    