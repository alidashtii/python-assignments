if condition:
		'code'
elif condition2:
		'code'
else:
	'another code'

		


for item in items:
	print 'str'

for item in range(1,10) : print item


counter = 0
while condition:
	print 'str'
	counter = counter + 1
							

while condition : print 'str'

tutorialspoint.com


'str %s' ' % ('my name')
'str {}' .format('my name')


def funcname():
	code
		
def funcname():
	return

def funcname():
	return var

def funcname(*args):
	print args

def funcname(**kwargs):
	print kwargs


lambda in1, in2 : in1+in2

import modulename

from modulename import func , class or ...

import module name as module

from modulename import func as f
	
from modulename import *


sudo nano __init__.py #for creating package

name.append() # ezafe mikone 1 done item

len() # tool ro barmigardone

cmp() # compare mikone

list(string)   # tabdil be reshte mikone sring ro

 name.count(x) # tedade x ro to name mishmore

 name.index(x) # mige x chandomin onsore name e

 name.insert(jash,meghdar)

 name.pop(jaye item morede nazar) # mindaze birun va hazf mikone

 name.remove(value) 

 name.reverse() # barax mikone

 name.sort()

() ==> tuple 

write read 

r ==> faghat baraye khandan. agar file mojod nabashad error midahad

r+ ==> ham baraye khandan va ham baraye neveshtan. agar file mojod nabashad errror midahad

w ==> faghat dastrasi neveshtan . agar file mojod nabashad error nemidahad va an r baraye ma misazad . agar file mojod bashad mohtava baznevisi mishavad

w+ ==> ham dastrasi khandan ham neveshtan. baghie mesl w

a ==> matn morede nazar ra dar akhar file minevisad.agar file mojod nabashad error nemidahad va an ra baraye ma misazad

a+ ==> manand a ba fargh inke dastrasi neveshtan ham midahad

f.mode() ==> toye r w ya ... ?

f.name() ==> masir file

f.tell() ==> jaye pointer to file

f.seek(jaye pointer, 0=nesbat be aval file 1=nesbat be jayi ke hastim 2=nesbat be akhare file) ==> pointer ro pas midim be harja az file ke mikhaym

 import os 
 os.getcwd() ==> to koja dare ejra mishmore

 os.chdir(masir) ==> change directory mikone

 os.rename('' , '')

 os.remove('')

 os.mkdir('esm folder')

 os.rmdir('esm directory')

 f.readline()

 f.readline() ==> har khat az file maro be onvane ye onsor mirize to list



from datetime import datetime



 __gt__ >
 __lt__ <
 __eq__ ==
 __ne__ !=
 __gt__ >=
 __le__ <=

from functools import total_ordering
@total_ordering

mutables:
	list
	set
	dict
	class 
	classinstance
	bytarray

immutables
	int
	float
	complex
	str
	tuple
	bytes
	bool
	frozenset

	dict ==> {key : value}

		dict.fromkeys ( key , [value.optional])
		dict.has_key(key) ==> true or false
		dict.items ==> return all
		b.update(c) ===> itemaye c ro be b ezafe mikone
		

	set
		set()
		set.clear() ==> delete all items
		set.add(item) ==> item ro ezafe mikone 1 vorodi!




	======= assertion =====
	#before
	def kelvintofahrenheit(temperature):
		assert (temperature >= 0) , '' colder than absolute zero!''
		return ((temperature - 273)*1.8) +32
	#after
	assert (kelvintofahrenheit(-3) < 10)




=====exeption====


try:
	pass
except [exception]:
	pass
else:
	pass
finally:
	pass
	


def get_key_or_index (var , index):
	try:
		result = int(var[index])
	except IndexError:
		print 'index error'
	except KeyError:
		print 'Key error'
	except TypeError:
		print 'enter valid input'
	else:
		return result
	return

	raise error , 'error message' ==> error mindaze

	#example
class Error(Exception):
		"""Base class for othe exceptions"""
	pass

class ValueTooSmallError(Error):
		""" raised when the input value is to small"""
	pass

class ValueTooLargeError(Error):
		"""raised wgen the input value is too large"""
	pass

while true:
	try:
		i_num = int(input('enter a number:'))
		if i_num < number:
			raise ValueTooSmallError
		elif i_num > number:
			raise ValueTooLargeError
		break
	except ValueTooSmallError:
		print ('this value is to small , try again!')
		print()
	except ValueTooLargeError:
		print ('this value is to large , try again!')
		print()





===== generator ====

#exp 1
def func():
	yield 1
	yield 2
	yield 3

#exp2
def func():
	i = 1
	while true:
		yield i * 2
		i+=1
























