import random
a = random.randint(1,9)
b = int(input('pls enter a number in range 1 - 9 : '))
while b != a
	if b > a:
		print ('too high')
	elif b < a:
		print (' too low')
	else:
		print ('exactly right')
		
