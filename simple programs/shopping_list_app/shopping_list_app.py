# Filename: shopping_list_app.py
# Versions
# A simple python programming app that showcases use of:
#      - list
#      - loops   
#      - user input
# What it does:
#      - Takes all that items you want to buy and stores in a list.
#      - Once list is done, "DONE" should be entered to quit the app
#      - Once quit is triggered by user, it displays all the items on the list

print("Hi! Welcome to this simple shopping list app.")
print("Please enter 'DONE' to exit. Happy shopping!")
item_list = []

while True:
  user_input = input("Enter item: ")
  
  if user_input == "DONE":
    break;
  
  item_list.append(user_input)
  
print("Here's your shopping list: ")
print("="*20)
for item in item_list:
  print("  >>" + item)
  
print("="*20)