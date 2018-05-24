number = input ('enter a number:')
factorial = 1
if number < 0:
	print ('we cant get factorial of negetive numbers')
elif number == 0:
	print ('factorial of zero is 1')
else:
	for i in range (1 , number +1):
		factorial = factorial * i
	print (factorial)


	

