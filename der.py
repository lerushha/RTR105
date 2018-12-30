from matplotlib import pyplot as plt
from numpy import arctan, linspace


def f(x):
    return arctan(x)

x = linspace(0, 4, 11)
print(x)
y = f(x)
print(y)

firstder = [] #1. kārtas atvasinājums
deltax = x[1] - x[0]
N = len(x)

for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    firstder.append(temp)

secondder = [] #2. kārtas atvasinājums

for i in range(N - 1):
    temp = (firstder[i + 1] - firstder[i]) / deltax
    secondder.append(temp)

legend = []

plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("$arctan(x)$ funkcija in tas atvasinājumi")

plt.plot(x, y, "k")
legend.append("$arctan(x) f-cija$")
plt.plot(x, y, "go")
legend.append("$arctan(x) f-cija(punkti)$")

plt.plot(x, firstder, "m")
legend.append("$arctan(x)$ 1.k. atvasinājums")
plt.plot(x, firstder, "ro")
legend.append("$arctan(x)$ 1.k. atvas.(punkti)")

plt.plot(x[0:len(x) - 1], secondder, "b")
legend.append("$arctan(x)$ 2.k. atvasinājums")
plt.plot(x[0:len(x) - 1], secondder, "ko")
legend.append("$arctan(x)$ 2.k. atvas.(punkti)")


plt.legend(legend, loc=3) #legendas atraš.vieta

plt.show() #attēlot gr.
