def fibo():

	num = int(input("how many fibonnaci numbers to generate:"))
	i = 1
	if num == 0:
		fib = []
	elif num == 1:
		fib = [1]
	elif num == 2:
		fibb = [1,1]
	elif num > 2:
		fib = [1,1]
		while i < (num -1):
			fib = [fib[i] + fib[i-1]]
			i+=1
	return fib
	

	

