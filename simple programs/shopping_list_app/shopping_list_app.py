# Filename: shopping_list_app.py
# Versions
# A simple python programming app that showcases use of:
#	- lists
#	- loops
#	- functions
#	- user input
# Features:
#	- add items
#	- show items
#	- exit
#	- show help

print("Hi! Welcome to this simple shopping list app.")
print("Type 'HELP' and <enter> for more options.")
print("Start listing now...")

item_list = []

def show_list_items():
	print("Here's your list: ")
	print("="*30)
	for item in item_list:
		print("   - " + item)
	print("="*30)
	
def show_help():
	print(("="*11) + "HELP" + ("="*11))
	print("You may type the following and press <enter>: ")
	print("'HELP' - show help menu")
	print("'SHOW' - show current list")
	print("'DONE' - save list and exit app")
	print("="*30)

while True:
	user_input = input("	>")
  
	if user_input == "DONE":
		show_list_items()
		break
	elif user_input == "SHOW":
		show_list_items()
	elif user_input == "HELP":
		show_help()
	else:
		item_list.append(user_input)
