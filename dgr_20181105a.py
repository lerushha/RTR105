Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> str1="Hello"
>>> str2='there'
>>> bob=str1+str2
>>> print(bob)
Hellothere
>>> str='123'
>>> str3='123'
>>> str=str3+1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str=str3+1
TypeError: must be str, not int
>>> str3='123'
>>> str3=str3+1
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    str3=str3+1
TypeError: must be str, not int
>>> x=int(str3)+1
>>> print(x)
124
>>> name=input('Enter:')
Enter:Lera
>>> print(name)
Lera
>>> apple=input('Enter:')
Enter:290
>>> x=apple-19
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x=apple-19
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x=int(apple)-19
>>> print(x)
271
>>> fruit='banana'
>>> letter=fruit[1]
>>> print(letter)
a
>>> x=3
>>> w=fruit[x-1]
>>> print(w)
n
>>> zot='abc'
>>> print(zot[5])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> fruit='banana'
>>> print(len(fruit))
6
>>> fruit='pineapple'
>>> print(len(fruit))
9
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
0 b
1 a
2 n
3 a
4 n
5 a
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
b
a
n
a
n
a
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/dgr_20181105.py", line 15, in <module>
    while index<len(fruit):
NameError: name 'fruit' is not defined
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
b
a
n
a
n
a
b
a
n
a
n
a
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
Traceback (most recent call last):
  File "/home/user/RTR105/dgr_20181105.py", line 26, in <module>
    cout=cout+1
NameError: name 'cout' is not defined
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
3
>>> s='Monty Python'
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Python
>>> print(s[1:19])
onty Python
>>> a='Hello'
>>> b=a+'There'
>>> print(b)
HelloThere
>>> c=a+''+'There'
>>> print(c)
HelloThere
>>> fruit='banana'
>>> 'n''in fruit
SyntaxError: EOL while scanning string literal
>>> 'n' in fruit
True
>>> 'm' is fruit
False
>>> 'a' is fruit
False
>>> 'nan' is fruit
False
>>> 'a' in fruit
True
>>> 'nan' in fruit
True
>>> if 'a' in fruit:
	print('Found it!')

Found it!
>>> 
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
3
Traceback (most recent call last):
  File "/home/user/RTR105/dgr_20181105.py", line 29, in <module>
    if word=='banana':
NameError: name 'word' is not defined
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
3
Traceback (most recent call last):
  File "/home/user/RTR105/dgr_20181105.py", line 29, in <module>
    if word=='banana':
NameError: name 'word' is not defined
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
3
Traceback (most recent call last):
  File "/home/user/RTR105/dgr_20181105.py", line 29, in <module>
    if word=='banana':
NameError: name 'word' is not defined
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
3
All right,bananas.
Traceback (most recent call last):
  File "/home/user/RTR105/dgr_20181105.py", line 32, in <module>
    if world<'banana':
NameError: name 'world' is not defined
>>> 
================= RESTART: /home/user/RTR105/dgr_20181105.py =================
3
All right,bananas.
All right, bananas
>>> greet='Hello Igorj'
>>> zap=greet.lower()
>>> print(zap)
hello igorj
>>> print(greet)
Hello Igorj
>>> stuff='Hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> fruit='banana'
>>> pos=fruit.find('na')
>>> print(pos)
2
>>> aa=fruit.rind('z')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    aa=fruit.rind('z')
AttributeError: 'str' object has no attribute 'rind'
>>> aa=fruit,find('z')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    aa=fruit,find('z')
NameError: name 'find' is not defined
>>> aa=fruit.find('z')
>>> print(aa)
-1
>>> greet='Hello Mark'
>>> nnn=greet.upper()
>>> print(nnn)
HELLO MARK
>>> www=greet.lower()
>>> print(www)
hello mark
>>> greet='Hello Bob'
>>> nstr=greet.replace('Bob','Jane')
>>> print(nstr)
Hello Jane
>>> nstr=greet.replace('o','X')
>>> print(nstr)
HellX BXb
>>> greet='Hello Bob'
>>> greet.lstrip()
'Hello Bob'
>>> greet.rstrip()
'Hello Bob'
>>> greet.strip()
'Hello Bob'
>>> line='Please give me fome food'
>>> line.startwith('ģive')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    line.startwith('ģive')
AttributeError: 'str' object has no attribute 'startwith'
>>> line.startswith('Please')
True
>>> line.startswith(give)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    line.startswith(give)
NameError: name 'give' is not defined
>>> line.startswith(p)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    line.startswith(p)
NameError: name 'p' is not defined
>>> line.startswith(p)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    line.startswith(p)
NameError: name 'p' is not defined
>>> line.startswith('p')
False
>>> line.startswith('give')
False
>>> data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos=data.find('@')
>>> print(atpos)
21
>>> sppos=data.find('',atpos)
>>> print(sspos)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    print(sspos)
NameError: name 'sspos' is not defined
>>> print(sppos)
21
>>> sppos=data.find('',atpos)
>>> sppos=data.find(' ',atpos)
>>> print(sppos)
31
>>> hosp=data[atpos+1:sppos]
>>> print(host)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print(host)
NameError: name 'host' is not defined
>>> host=data[atpos+1:sppos]
>>> print(host)
uct.ac.za
>>> x='이광춘'
>>> type(x)
<class 'str'>
>>> x=u'이광춘'
>>> type(x)
<class 'str'>
>>> 
