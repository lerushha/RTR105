Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__.doc__

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __builtins__.doc__
AttributeError: 'module' object has no attribute 'doc__'
>>> 
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> a = 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 10, '__package__': None}
>>> a = 20
>>> b=1.56
>>> vars()
{'a': 20, 'b': 1.56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> c = 'Q'
>>> vars()
{'a': 20, 'c': 'Q', 'b': 1.56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> a*a
400
>>> b*b
2.4336
>>> a*b
31.200000000000003
>>> c*c

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c*c
TypeError: can't multiply sequence by non-int of type 'str'
>>> type(a)
<type 'int'>
>>> type(b)
<type 'float'>
>>> type(c)
<type 'str'>
>>> c*a*a
'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ'
>>> 
