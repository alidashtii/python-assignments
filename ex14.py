def func():
	lst = list(input('enter a list:'))
	st = set(lst)
	lst1 = list(st)
	print (lst1)
# Write a function that takes a list and returns a new list that contains 
# all the elements of the first list minus duplicates.
def dedupe_v2(x):
    return list(set(x))
