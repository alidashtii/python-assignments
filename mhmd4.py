import math
c = 50
h = 30
output = []
vorodi = list(input('enter numbers seperate by comma :').split(','))
for d in vorodi:
	output.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
	
print (output)