def mouse_party(cigars,is_weekend):
	if cigars<40 :
		return False
		
	elif cigars>= 40 and cigars <= 60:
		print ('123')
		return True
		
	else:
		
		return is_weekend
def str2bool(v):
  return v.lower() in ("yes", "true", "t")


cigars=int(input('tedad cigar :'))
get=input('is weekend? type true or false :')
is_weekend = str2bool(get)


print(mouse_party(cigars,is_weekend))
