
number = [x for x in input('enter 4 digit binary numbers seperate by comma : ').split(',')]
bnumber=[]
for num in number:
    x = int(num, 2)
    if not x%5:
        bnumber.append(num)
print(','.join(bnumber))


def bin_to_dec(x):
	return int(x,2)
def dec_to_bin(x):
    return bin(x)[2:]
