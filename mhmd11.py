number = input('enter 4 digit numbers seperate by comma :  ').split(',')
answer=[]
for num in number:
	if int(num)%5 == 0:
		answer.append(num)

print (answer)