input_str = input('enter 2 number split by comma : ').split(',')
dimensions=[int(x) for x in input_str]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist =[[0 for col in range(colNum)] , [0 for row in range(rowNum)]]

for row in range(rowNum):
    for col in range(colNum):
       	multilist[row][col]= row*col

print (multilist)