#vorodi begire sort kone
def sort(List):
	List.sort()
	return (List)

words=[x for x in raw_input('enter comma seperate words :').split(',')]

print (sort(words))