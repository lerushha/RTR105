Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> name=input('tests.1.py:')
tests.1.py:

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name=input('tests.1.py:')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> name=input('Enter file name:')
Enter file name: tests1.py

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    name=input('Enter file name:')
  File "<string>", line 1, in <module>
NameError: name 'tests1' is not defined
>>> name=input('Enter name:')
Enter name:tests1.py

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    name=input('Enter name:')
  File "<string>", line 1, in <module>
NameError: name 'tests1' is not defined
>>> name

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name=input('Enter name:')
Enter name:tests1.py

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    name=input('Enter name:')
  File "<string>", line 1, in <module>
NameError: name 'tests1' is not defined
>>> name=raw_input('Enter fale name:')
Enter fale name:tests1.py
>>> handle=open(name, 'r')
>>> handle
<open file 'tests1.py', mode 'r' at 0x7f95381c7e40>
>>> handle=open('tests1.py', 'r')
>>> handle
<open file 'tests1.py', mode 'r' at 0x7f95383378a0>
>>> counts=dict()
>>> for line in handle:
	words=line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1

		
>>> bigcount=None
>>> bigword=None
>>> for word,count in counts.items():
	if bigcount is None or count>bigcount:
		bigword=word
		bigcount=count

		
>>> print(bigword, bigcount)
('d', 2)
>>> 
