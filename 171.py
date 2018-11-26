from math import atan, fabs
from time import sleep

def f(x):
    return atan(x)
k=0
a = 1.1
b = 3.2

funa = f(a)
funb = f(b)

if (funa*funb>0.0):
    print ("Dotaja intervala [%s, %s] saknju nav" %(a,b))
    sleep(1); exit()
else:
    print ("Dotaja intervala sakne(s) ir!")

deltax = 0.0001

while (fabs(b-a)>deltax):
    k=k+1
    x=(a+b)/2; funx=f(x)
    if (funa*funx < 0.):
        b=x       
    else:
        a=x
print ("Sakne ir:", x)
print ("y=", atan(x))
print ("k=", k)

