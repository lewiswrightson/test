#Exercise 1 python basics

# 1

 course ='python'
>>> rating = 10
>>> print(course)
python
>>> print(rating)
10

#2
>>> a=((b**2 + c**2)**0.5)
>>> a
5.0

#3

#a is a float because it is a decimal number
>>> type(a)
<class 'float'>
>>> type(b)
<class 'int'>
>>> type(c)

#4
> a=int(a)
>>> type(a)
<class 'int'>

>>> print(a + "squared equals" + b + "squared +" + c + "squared.")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a=str(a)
>>> b=str(b)
>>> c=str(c)
>>> print(a + "squared equals" + b + "squared +" + c + "squared.")
5squared equals3squared +4squared.
>>> print(a + " squared equals " + b + " squared + " + c + " squared.")
5 squared equals 3 squared + 4 squared.

>>> print(str(a) + " squared equals " + str(b) + " squared + " + str(c) + " squared.")
5 squared equals 3 squared + 4 squared.

