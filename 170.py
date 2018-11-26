#Aptuveni novērtējot funkcijas saknes vērtību lietojot ”peli” iegūstam x=3,1346.

from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)
k=0
a = 1.1
b = 3.2

funa = f(a)
funb = f(b)

if (funa*funb>0.0):
    print ("Funkcijas sin(x) dotaja intervala [%s, %s] saknju nav" %(a,b))
    sleep(1); exit()
else:
    print ("Funkcijas sin(x) dotaja intervala sakne(s) ir!")

deltax = 0.001

while (fabs(b-a)>deltax):
    k=k+1
    x=(a+b)/2; funx=f(x)
    if (funa*funx < 0.):
        b=x       
    else:
        a=x
print (" sin(x) Sakne ir:", x)
print ("y=", sin(x))
print ("k=", k)
