def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
def factorial(n):
	fact = 1
	if n < 0:
		print ('we cant get factorial of negetive numbers')
	elif n == 0:
		print ('factorial of zero is 1')
	else:
		for i in range (1 , n +1):
			fact= fact * i
	print (n,fact)