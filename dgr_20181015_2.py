Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x=5
>>> if x<10:
	print('Smaller)
	      
SyntaxError: EOL while scanning string literal
>>> if x<10:
	print('Smaller')
	if x>20:
		print('Bigger')
		print('Finis')

		
Smaller
>>> 6
6
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_1.py ===============
Smaller
Finis
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_1.py ===============
Bigger
Finis
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_1.py ===============
Finis
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_1.py ===============
Bigger or equal
Finis
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_2.py ===============
Smaller
Finis
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_2.py ===============
Finis
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_2.py ===============
Bigger
Finis
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_3.py ===============
Eguals 5
Greater than 4
Greater than or Eguals 5
Less than 6
Less than or Equals 5
Not equal 6
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Before 5
Is 5
Is still 5
Third 5
Afterwarda 5
Before 6
Afterwards 6
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Before 5
Is 5
Is still 5
Third 5
Afterwards 5
Before 6
Afterwards 6
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_5.py ===============
Bigger than 2
Still bigger
Done with 2
0
('Done with i', 0)
1
('Done with i', 1)
2
('Done with i', 2)
3
Bigger than 2
('Done with i', 3)
4
Bigger than 2
('Done with i', 4)
All Done
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_6.py ===============
Bigger
All done
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_6.py ===============
Smaller
All done
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_7.py ===============

Traceback (most recent call last):
  File "/home/user/RTR105/test_20181015_7.py", line 1, in <module>
    if x<2:
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_7.py ===============
medium
All done
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_7.py ===============
medium
All done
>>> 
====================== RESTART: /home/user/RTR105/8.py ======================

Traceback (most recent call last):
  File "/home/user/RTR105/8.py", line 1, in <module>
    if x<2:
NameError: name 'x' is not defined
>>> 
====================== RESTART: /home/user/RTR105/8.py ======================
medium
>>> 
====================== RESTART: /home/user/RTR105/8.py ======================
('first', -1)
('second', 123)
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Enter a nember:5
Nice work
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
Enter your hours: 45
Enter your rate: 10
475.0
>>> 
=============== RESTART: /home/user/RTR105/test_20181015_4.py ===============
enter hours:20
Enter rate per hour: nine
Error, please enter numeric input
>>> 
