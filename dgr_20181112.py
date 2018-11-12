Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a='Hello\nWorld!'
>>> a
'Hello\nWorld!'
>>> print(a)
Hello
World!
>>> a='Hello\nWorld!'
>>> fhand=open('mbox.txt')
>>> count=0
>>> for line in fhand:
	count=count+1
print('Line Count:', count)
SyntaxError: invalid syntax
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
Line Count: 5
>>> fhand=open('mbox-short.txt')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fhand=open('mbox-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> fhand=open('mbox.txt')
>>> inp=fhand.read()
>>> print(len(inp))
55
>>> print(inp[:20])
jhjfhoshfoshfshfjsdh
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
jhjfhoshfoshfshfjsdhjkfhdsjkh

>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
Traceback (most recent call last):
  File "/home/user/RTR105/test_20181112.py", line 25, in <module>
    for line in fland:
NameError: name 'fland' is not defined
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
Traceback (most recent call last):
  File "/home/user/RTR105/test_20181112.py", line 27, in <module>
    if line.startswint('jhj'):
AttributeError: 'str' object has no attribute 'startswint'
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
Traceback (most recent call last):
  File "/home/user/RTR105/test_20181112.py", line 27, in <module>
    if line.startswint('jhj'):
AttributeError: 'str' object has no attribute 'startswint'
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
jhjfhoshfoshfshfjsdhjkfhdsjkh
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
Traceback (most recent call last):
  File "/home/user/RTR105/test_20181112.py", line 33, in <module>
    line=line.rstip()
AttributeError: 'str' object has no attribute 'rstip'
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
jhjfhoshfoshfshfjsdhjkfhdsjkh
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
jhjfhoshfoshfshfjsdhjkfhdsjkh
>>> 
================ RESTART: /home/user/RTR105/test_20181112.py ================
Enter the file name: mbox.txt
There were 0 subject lines in mbox.txt
>>> 
