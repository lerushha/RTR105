from math import atan
import math

def mans_atan(x):
    k = 0
    a = (1/(1**2*4**0*(2*0+1)))*((x**2/(1+x**2))**0)
    S = a
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 500:
      k = k + 1
      R= (((2*k-1)**2)/(2*(2*k+1)))*((x**2)/(1+x**2))
      a = a * R
      S = S + a
      if k == 499 :
        print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
    print("Izdruka no liet.f. a500 = %6.2f S500 = %6.2f"%(a,S))
    S=(x/math.sqrt(1+x**2))*S
    return S

x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = atan(x)
print("standarta atan(%.2f) = %6.2f"%(x,y))
                   
yy = mans_atan(x)
print("mans atan(%.2f) = %6.2f"%(x,yy))



print("                        500                                    ")
print("                      _______                                  ")
print("                x     \                                   2 k  ")
print("              ______   \           (2*k)!             ( x  )   ")
print("atan(%.2f)=   _____    \ _____________________* ___________    "%(x))
print("              /   2     /         2  k                      2 k")
print("            \/ 1+x     /      (k)! *4 *(2*k+1)        (1+(x))  ")
print("                      /______                                  ")
print("                         k=0                                   ")


print("                              2       2  ")
print("                        (2*k-1)      x   ")
print("rekurences reizinatajs:___________*______")
print("                        2*(2*k+1)      2 ")
print("                                    1+x  ")




      
