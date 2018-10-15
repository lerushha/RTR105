'''
x = 20

if x<10:
    print('Smaller')
if x>=20:
    print('Bigger or equal')

print('Finis')
'''

'''
x=21

if x<10:
    print('Smaller')
if x>=20:
    print('Bigger')
    
print('Finis')
'''

'''
x=5
if x==5:
    print('Eguals 5')
if x>4:
    print('Greater than 4')
if x>=5:
    print('Greater than or Eguals 5')
if x<6:
    print('Less than 6')
if x<=5:
    print('Less than or Equals 5')
if x!=6:
    print('Not equal 6')
'''

'''
x=5
print('Before 5')
if x==5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x==6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 6')
'''

'''
x=5
if x>2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i>2:
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')
'''

'''
x=1
if x>2:
    print('Bigger')
else:
    print('Smaller')
print('All done')
'''

'''
x=900

if x<2:
    print('small')
elif x>10:
    print('medium')
else x>50:
    print('large')
print('All done')
'''

'''
x=5

if x<2:
    print('Small')
elif x<10:
    print('medium')
elif x>20:
    print('big')
elif x>40:
    print('large')
elif x<100:
    print('huge')
else:
    print('ginormous')
'''

'''
astr='Hello Bob'
try:
    istr=int(astr)
except:
    istr=-1
print('first', istr)

astr='123'
try:
    istr=int(astr)
except:
    istr=-1

print('second', istr)
'''

'''rawstr=input('Enter a nember:')
try:
    ival=int(rawstr)
except:
    ival=-1

if ival>0:
    print('Nice work')
else:
    print('Not a number')
'''

'''
hrs=input('Enter your hours: ')
h=float(hrs)
rate=input('Enter your rate: ')
r=float(rate)
if h>40:
    pay=40*r+(h-40)*15
else:
    pay=h*r
print(pay)
'''

'''

try:
    hrs = input('enter hours:')
except:
    hr='Error, please enter numeric input'
    print(hr)
try:
    rate=input('Enter rate per hour: ')
except:
    rt='Error, please enter numeric input'
    print(rt)
'''
    
