# Filename: reverse_evens.py
# Versions: Python 3
# A simple python exercise that accepts a single iterable as an argument. Return every item in the iterable with an even index...in reverse.
# For example, with [1, 2, 3, 4, 5] as the input, the function would return [5, 3, 1].
#	- functions
#	- list slice method

def rev_evens(iterable):
	return iterable[-2::-2] if len(iterable) % 2 == 0 else iterable[-1::-2]

	
#	print("len(iterable): {}".format(len(iterable)))
#	if len(iterable) % 2 == 0:
#		print("len is even")
#		it = iterable[-1::-2]
#		print(', '.join(str(x) for x in it))
#	else:
#		print("len is odd")
#		it = iterable[-2::-2]
#		print(', '.join(str(x) for x in it))
#	
#	print("\nFinal: ")
#	return it	

print(', '.join(str(x) for x in rev_evens([1,2,3,4,5])))