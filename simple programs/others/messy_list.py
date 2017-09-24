# Filename: messy_list.py
# Versions: Python 3
# A simple python exercise which aims to remove non-integer values from a given list
#	- loop
#	- str join
#	- type()
#	- list methods

messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
messy_list.insert(0,messy_list.pop(3))

print(', '.join(str(x) for x in messy_list))

for i in list(messy_list):
	if type(i) != int:
		messy_list.remove(i)
		
print(', '.join(str(x) for x in messy_list))