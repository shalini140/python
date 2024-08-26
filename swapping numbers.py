Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def swap_with_temp(a,b):
	temp=a
	a=b
	b=temp
	return a,b

>>> a=10
>>> b=20
>>> print("before swap(with temp):",a,b)
before swap(with temp): 10 20
>>> a,b=swap_with_temp(a,b)
>>> print("after swap(with temp):",a,b)
after swap(with temp): 20 10
>>> def swap_without_temp(a,b):
	a,b=b,a
	return a,b

>>> a=10
>>> b=30
>>> print("before swap(without temp):",a,b)
before swap(without temp): 10 30
>>> a,b=swap_without_temp(a,b)
>>> print("after swap(without temp):",a,b)
after swap(without temp): 30 10
>>> 
