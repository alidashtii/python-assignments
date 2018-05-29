def mouse_party(cigars,is_weekend):
	if cigars<40 :
		print ('false')
		
	elif cigars>= 40 & cigars <= 60:
		print ('true')
		
	else:
		if is_weekend == false:
			print (false)
			
		else:
			print (true)
			
cigars=int(input('tedad cigar :'))
is_weekend=input('is weekend? type true or false :')
mouse_party(cigars,is_weekend)