Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from math import *
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'acos': <built-in function acos>, 'acosh': <built-in function acosh>, 'asin': <built-in function asin>, 'asinh': <built-in function asinh>, 'atan': <built-in function atan>, 'atan2': <built-in function atan2>, 'atanh': <built-in function atanh>, 'ceil': <built-in function ceil>, 'copysign': <built-in function copysign>, 'cos': <built-in function cos>, 'cosh': <built-in function cosh>, 'degrees': <built-in function degrees>, 'erf': <built-in function erf>, 'erfc': <built-in function erfc>, 'exp': <built-in function exp>, 'expm1': <built-in function expm1>, 'fabs': <built-in function fabs>, 'factorial': <built-in function factorial>, 'floor': <built-in function floor>, 'fmod': <built-in function fmod>, 'frexp': <built-in function frexp>, 'fsum': <built-in function fsum>, 'gamma': <built-in function gamma>, 'gcd': <built-in function gcd>, 'hypot': <built-in function hypot>, 'isclose': <built-in function isclose>, 'isfinite': <built-in function isfinite>, 'isinf': <built-in function isinf>, 'isnan': <built-in function isnan>, 'ldexp': <built-in function ldexp>, 'lgamma': <built-in function lgamma>, 'log': <built-in function log>, 'log1p': <built-in function log1p>, 'log10': <built-in function log10>, 'log2': <built-in function log2>, 'modf': <built-in function modf>, 'pow': <built-in function pow>, 'radians': <built-in function radians>, 'sin': <built-in function sin>, 'sinh': <built-in function sinh>, 'sqrt': <built-in function sqrt>, 'tan': <built-in function tan>, 'tanh': <built-in function tanh>, 'trunc': <built-in function trunc>, 'pi': 3.141592653589793, 'e': 2.718281828459045, 'tau': 6.283185307179586, 'inf': inf, 'nan': nan}
>>> 
=========== RESTART: /home/user/RTR105/teilora_rindas_versija1.py ===========
Lietotāj, lūdzu, ievadi argumentu (x): 7
Traceback (most recent call last):
  File "/home/user/RTR105/teilora_rindas_versija1.py", line 2, in <module>
    y = sin(x)
NameError: name 'sin' is not defined
>>> from math import sin
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/teilora_rindas_versija1.py', 'x': 7.0, 'sin': <built-in function sin>}
>>> 
=========== RESTART: /home/user/RTR105/teilora_rindas_versija1.py ===========
Lietotāj, lūdzu, ievadi argumentu (x): 9
Traceback (most recent call last):
  File "/home/user/RTR105/teilora_rindas_versija1.py", line 2, in <module>
    y = sin(x)
NameError: name 'sin' is not defined
>>> 
=========== RESTART: /home/user/RTR105/teilora_rindas_versija1.py ===========
Lietotāj, lūdzu, ievadi argumentu (x): 9
sin(9.00) = 0.41
a0 = 9.00 S0 = 9.00
a1 = -121.50 S1 = -112.50
a2 = 492.07 S2 = 379.57
a3 = -949.00 S3 = -569.43
>>> 
=========== RESTART: /home/user/RTR105/teilora_rindas_versija1.py ===========
Lietotāj, lūdzu, ievadi argumentu (x): 
Traceback (most recent call last):
  File "/home/user/RTR105/teilora_rindas_versija1.py", line 4, in <module>
    x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
ValueError: could not convert string to float: 
>>> 
=========== RESTART: /home/user/RTR105/teilora_rindas_versija1.py ===========
Lietotāj, lūdzu, ievadi argumentu (x): 1.345
sin(1.34) = 0.97
a0 = 1.34 S0 = 1.34
a1 = -0.41 S1 = 0.94
a2 = 0.04 S2 = 0.98
a3 = -0.00 S3 = 0.97
>>> 
=========== RESTART: /home/user/RTR105/teilora_rindas_versija1.py ===========
Lietotāj, lūdzu, ievadi argumentu (x): 1.222
sin(1.22) = 0.94
a0 = 1.22 S0 = 1.22
a1 = -0.30 S1 = 0.92
a2 = 0.02 S2 = 0.94
a3 = -0.00 S3 = 0.94
>>> 
=========== RESTART: /home/user/RTR105/teilora_rindas_versija1.py ===========
Lietotāj, lūdzu, ievadi argumentu (x): 0
sin(0.00) = 0.00
a0 = 0.00 S0 = 0.00
a1 = -0.00 S1 = 0.00
a2 = 0.00 S2 = 0.00
a3 = -0.00 S3 = 0.00
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver2.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 0.344
sin(0.34) = 0.34
a0 = 0.34 S0 = 0.34
a1 = -0.01 S1 = 0.34
a2 = 0.00 S2 = 0.34
a3 = -0.00 S3 = 0.34
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver2.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 1,890
Traceback (most recent call last):
  File "/home/user/RTR105/sin_caur_summ_ver2.py", line 4, in <module>
    x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
ValueError: could not convert string to float: '1,890'
>>> 1.890
1.89
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver2.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 1.890
sin(1.89) = 0.95
a0 = 1.89 S0 = 1.89
a1 = -1.13 S1 = 0.76
a2 = 0.20 S2 = 0.97
a3 = -0.02 S3 = 0.95
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver3.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 1.345
sin(1.34) =   0.97
a0 =   1.34 S0 =   1.34
a1 =  -0.41 S1 =   0.94
a2 =   0.04 S2 =   0.98
a3 =  -0.00 S3 =   0.97
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver3.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 5.987
sin(5.99) =  -0.29
a0 =   5.99 S0 =   5.99
a1 = -35.77 S1 = -29.78
a2 =  64.10 S2 =  34.32
a3 = -54.71 S3 = -20.38
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver3.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 2.777
sin(2.78) =   0.36
a0 =   2.78 S0 =   2.78
a1 =  -3.57 S1 =  -0.79
a2 =   1.38 S2 =   0.58
a3 =  -0.25 S3 =   0.33
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver3.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 2.123
sin(2.12) =   0.85
a0 =   2.12 S0 =   2.12
a1 =  -1.59 S1 =   0.53
a2 =   0.36 S2 =   0.89
a3 =  -0.04 S3 =   0.85
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver4.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 1.567
sin(1.57) =   1.00
a0 =   1.57 S0 =   1.57
a1 =  -0.64 S1 =   0.93
a2 =   0.08 S2 =   1.00
a3 =  -0.00 S3 =   1.00
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver4.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 4.666
sin(4.67) =  -1.00
a0 =   4.67 S0 =   4.67
a1 = -16.93 S1 = -12.27
a2 =  18.43 S2 =   6.17
a3 =  -9.55 S3 =  -3.39
>>> 1.234
1.234
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver4.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 1.234
sin(1.23) =   0.94
a0 =   1.23 S0 =   1.23
a1 =  -0.31 S1 =   0.92
a2 =   0.02 S2 =   0.94
a3 =  -0.00 S3 =   0.94
>>> 
============== RESTART: /home/user/RTR105/sin_caur_summ_ver5.py ==============
Lietotāj, lūdzu, ievadi argumentu (x): 1.368
standarta sin(1.37) =   0.98
Izdruka no liet.f. a0 =   1.37 S0 =   1.37
Izdruka no liet.f. a1 =  -0.43 S1 =   0.94
Izdruka no liet.f. a2 =   0.04 S2 =   0.98
Izdruka no liet.f. a3 =  -0.00 S3 =   0.98
Izdruka no liet.f. Beigas!
mans sin(1.37) =   0.98
>>> 
