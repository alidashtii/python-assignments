def func(n):
	mydict={}
	for i in range(1,n+1):
			mydict[i]= i*i

	return mydict

n = int(input('enter a number'))
print func(n)
