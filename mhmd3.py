class MyString:
	str = ""

	def getString(self):
		self.str = input('enter a string :  ')
	

	def printString(self):
		upper= self.str.upper()
		print(upper)



strObj = MyString()
strObj.getString()
strObj.printString()
		
		