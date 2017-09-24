# Filename: shopping_list_ap_v2.py
# Versions
# A simple python programming app that showcases use of:
#	- lists, list methods
#	- loops
#	- functions
#	- user input
#	- import libraries: os
# Features:
#	- add items
#	- show items
#	- exit
#	- show help
#	- delete
#	- clear screen
import os

print("Hi! Welcome to this simple shopping list app.")
print("Type 'HELP' and <enter> for more options.")
print("Start listing now...")

item_list = []

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def show_list_items():
	clear_screen()
	print("Here's your list: ")
	index = 1
	print("="*30)
	for item in item_list:
		print("   {}. {} ".format(index, item))
		index +=1
	print("="*30)
	
def show_help():
	clear_screen()
	print(("="*11) + "HELP" + ("="*11))
	print("You may type the following and press <enter>: ")
	print("'HELP' - show help menu")
	print("'SHOW' - show current list")
	print("'DONE' - save list and exit app")
	print("'REMOVE' - to delete an item from your list")
	print("="*30)
	
def remove_from_list():
	show_list_items()
	what_to_remove = input("what would you like to remove?\n     >")
	try:
		item_list.remove(what_to_remove)
	except ValueError:
		print("No such {} in the list".format(what_to_remove))
		pass	
	
def add_to_list(item):
	show_list_items()
	
	if len(item_list):
		position = input("Where should I add {}?\n"
		"Press ENTER to add to the end of the list\n"
		"	>".format(item))
	else:
		position = len(item_list) + 1
		
	try:
		position = abs(int(position))
	except ValueError:
		position = None
	
	if position is not None and position != 0:
		item_list.insert(position - 1, item)
	else:
		item_list.append(item)
	
	show_list_items()

def is_valid(item):
	return(bool(item))

	
while True:
	user_input = input("	>")
	
	if not is_valid(user_input):
		print("You can't add nothing to shopping list.")
		continue
	elif user_input.upper() == "DONE" or user_input.upper()== "QUIT":
		break
	elif user_input.upper() == "SHOW":
		show_list_items()
		continue
	elif user_input.upper() == "HELP":
		show_help()
		continue
	elif user_input.upper() == "REMOVE":
		remove_from_list()
		show_list_items()	
		continue
	else:
		add_to_list(user_input)

show_list_items()