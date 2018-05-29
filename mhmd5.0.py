#write a program that take 2 number and print multiple table
input_str = input('enter 2 number split by comma : ').split(',')
dimensions=[int(x) for x in input_str]
rowNum=dimensions[0]
colNum=dimensions[1]
def multi(row,col):
	multilist =[[row*col for col in range(colNum)] for row in range(rowNum)]
	return multilist
def printtable(list):
	for row in list:
		for col in row:
			print (col ,end='\t')
		print()
print (multi(rowNum,colNum))
printtable(multi(rowNum,colNum))