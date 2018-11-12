'''
>>> a='Hello\nWorld!'
>>> a
'Hello\nWorld!'
>>> print(a)
Hello
World!
>>> a='Hello\nWorld!'
'''
'''
fhand=open('mbox.txt')
count=0
for line in fhand:
	count=count+1
print('Line Count:', count)
'''
'''
fhand=open('mbox.txt')
for line in fhand:
    if line.startswith('jhj'):
        print(line)
'''
'''
fhand=open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('jhj'):
        print(line)
'''
'''
fhand=open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('jhj'):
        continue
    print(line)
'''
'''
fhand=open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    if not 'jhj'in line:
        continue
    print(line)
'''
'''
fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:', fname)
    guit()

count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were', count, 'subject lines in', fname)
'''
