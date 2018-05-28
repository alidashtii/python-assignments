#برنامه‌ای بنویس که یه لیست از اعداد که با کاما از هم جدا شدن را بعنوان ورودی بگیره از ترمینال و بعنوان خروجی یه لیست (list) و یه تاپل (tuple) از همه ی اون اعداد خروجی بده
def getnumber(n):
	a = list(n)
	b = tuple(n)
	return a,b


(a,b) = getnumber(input('type numbers seperate by comma: ').split(','))
print (a)
print (b)


