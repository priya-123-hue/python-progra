#wap to extract all the even no present in a list
'''
l=[10,23,6,1,8,14,19]
print([x for x in l if x%2==0])
'''

#wap to check whether the char is uppercase,lowercase,digitor special char.
'''
c=input("enter a character")
if c.isupper():
    print("it is uppercaase")
elif c.islower():
    print("it is in lowercase")
elif c.isdigit():
    print("digit")
else:
    print("special char")
    '''

#prime or not
'''
def check_prime(n):
    if n<2:
        print('it is not prime')
        return
    for i in range(2,n):
        if n%i==0:
            print('the no is not prime')
            return
    print('the no is prime')
check_prime(3)
'''
#flip binary
'''
n=input("enter binary no:")
r=''
for i in n:
    if i=='0':
        r+='1'
    elif i=='1':
        r+='0'
    else:
        r+=''
print(r)
'''

#datatypes
'''
a=10.
print(type(a))
b=1
print(type(b))
c=3+j
print(type(c))
'''


'''
username="priya2007"
password="priya@1323"
c=input("enter a username")

if c==username:
    print("logged in successfully")
else:
    print("invalid")
p=input(" enter password:")
if p==password:
    print("logged in successfully")
else:
    print("invalid")'''


#extract everyone and enjoy
'''
a='good morning everyone i hope you all enjoy python'
print(a[13:43])'''

#list: collection of homogenous and hetreogenous.
#mutable,slicing and indexing is possible 
#list as more inbuild function tuple as less
''' 
s=[1,2,3,'hello',(6,5,7),7.8]
print(len(s))
print(s[4][1]) #extract 5 from list l..
print(s[3])
print(s[3][2:4])
print(dir(tuple)) #it show the inbuild function 

'''

#tuple

'''
t=(1,2,3,[4,5,6],7,8)
print(t[4])
print(t[4].append(9))
'''

#set
'''
s={True,(1,2,3)}
print(s)
'''

#dictionary
'''
s={'a':1,'b':2,10:20,4.5:(6+7)}
print(s)
'''

# write a program to gift a watch if you have brand 
'''
a=int(input('enter mark:'))
if  a>70:
    print(' present a watch')
'''

# write a program to check whether  the char is vowel
'''
ch=input('enter a character')
if ch in  'aeiou':
    print('it is vowel')

ch=input('enter a character')
if ch  not in  'aeiou':
    print('it is con')
    '''



#write  a program to print the cube of the number if it is diisible by 3 and 5
'''
b=int(input('enter a no:'))
if b%3==0 & b%5==0:
    print('cube ',b**3)
    '''
# check whether the no is even or odd
'''
n=int(input('enter a no:'))
if n%2==0:
    print('it is even')
else:
    print('odd')
    '''
#write prgm  to chek given no mutable or not
'''
c=int(input('enter data:'))
if type(c) in [list,set,dict]:
    print('mutable')
else:
    print('immutable')
    '''

#special or not
'''
c=input('enetr ch')
if ('a'<=c<='z' or 'A'<=c<='Z' or c.isdigit()): #or if c.isalnum():
        print('not special')
else:
        print('special')
        '''

#homogenous or not wrong this is
''' 
a=eval(input('enter a list:'))
if type(a[0]==type(a[1])):
    print('homogeno')
else:
    print('not ')
    '''

# check whether the char is upper ,lower,,digit and special
'''
c=input("enter a character")
if c.isupper():
    print("it is uppercaase")
elif c.islower():
    print("it is in lowercase")
elif c.isdigit():
    print("digit")
elif ('a'<=c<='z' or 'A'<=c<='Z' or c.isdigit()): 
    print('special')
else:
    print("invalid")
    '''
#greatest of 3 no find
'''
a=2
b=8
c=4
if a>b and a>c:
    print('a is greater')
elif b>a and b>c:
    print('b is greater')
else:
    print('c is greater')

#wap to find in which quadrant x,y in
x=int(input('enter x:'))
y=int(input('enter y:'))
if x>0 or y>0:
    print('1 quadrant')
elif x<0 or y>0:
    print('2 quadrant')
elif x<0 or y<0:
    print('3 quadrant')
elif x>0 or y<0:
    print('4 quadrant')
    '''

#looping statements



#while loop
#1-10
'''
i=1
while(i<=10):
    print(i)
    i=i+1
'''

#10-1
'''
i=10
while(i>=1):
    print(i)
    i=i-1
'''

#multiplication
'''
n=int(input('enter a num:'))
i=1
while(i<=12):
    print(2,'*',i,'=',2*i)
    i+=1 
''' 

#list as ip and print all the element
'''
l=eval(input('enter the list elements:'))
i=0
while(i<len(l)):
    print(l[i])
    i+=1
    '''

#list as ip and print all the element
'''
l=eval(input('enter the list elements:'))
i=0
while(i<len(l)):
    if type(l[i])==int and  l[i]%2==0:
        print(l[i])
        i+=1
'''

#list as ip and extract all the element
'''
l=eval(input('enter the list elements:'))
a=[]
i=0
while(i<len(l)):
    if type(l[i])==int and l[i]%2==0:
        a.append(l[i])
    i+=1
print(a)
'''

#extract all vowel in ur name
'''
n=input('enter ur name:')
e=''
i=0
while(i<len(n)):
    if n[i] in 'aeiouAEIOU':
        e+=n[i]
    i+=1
print(e)
'''

#reverse a num without using typecasting
'''
n=int(input('enter a number:'))
r=0
while(n!=0):    
ld=n%10
    r=r*10+ld
    n=n//10
print(r)
'''

#sum of even amd pro os=f odd
'''
n=int(input('entera umber'))
s=0
p=1
r=0
while(n!=0):
    r=n%10
    if r%2==0:
        s+=r
    else:
        p*=r
    n=n//10

print(s,p)
'''


#for loop
#1-10
'''
for i in range(1,11):
    print(i,end=' ')
'''

#u-l and l-u
'''
s=input('enter a string:')
c=''
for i in s:
    if i.isupper():
        c+=i.lower()
    else:
        c+=i.upper()
print('converted string:',c)
print('aA'.swapcase()) # can use swapcase() too!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

#reverse a string without slicing
'''
s = input("Enter a string: ")
r = ""
for i in s:
    r = i + r
print("Reversed string:",r)
'''

#for loop
##write a program to find the length of a collection without len function.
'''
c=eval(input('enter a char:'))
a=0
for i in c:
    a+=1
print('count',a)
'''

#input:'python coder'
#output:{python:6,coder:5}
'''
a='python coder'
s=a.split()
d={}
for i in s:  #or use if .isalnum():
    print('enter :',i)
    d[i]=int(input('enter value:'))
print(d)
'''

#input= ['jiocinemas.com','file.py','web.html','amazon.com','www.org]
#output:['com','py','html','com','org']
'''
a=['jiocinemas.com','file.py','web.html','amazon.com','www.org']
s=[]
for i in a:
    a=i.split('.')
    s.append(a[-1])  
print(s)
'''

#input= ['jiocinemas.com','file.py','web.html','amazon.com','www.org]
#output:{'com':['jiocinemas','amazon'],'py':['file','python'],'html':['web'],'org':['www']}
# Output dictionary
'''
input= ['jiocinemas.com','file.py','web.html','amazon.com','www.org']
output = {}
for item in input:
    if '.' in item:
        name, ext = item.rsplit('.', 1)   # split into name and extension
        # special case: replace 'py' with 'python'
        if ext == 'py':
            ext = 'python'
        # add into dictionary
        output.setdefault(ext, []).append(name)
print(output)
'''

#nested for
#input:'python coder'
#output:{'python':'o','coder':'oe'}
'''
a='python coder'
d={}
for i in a.split():
    c=''
    for j in i:
        if j in 'aeiou':
            c+=j
        d[i]=c
print(d)
'''
# input='abcdacdcadc'
#output='a3b1c4d3'
input='abcdacdcadc'
a=0
b=0
c=0
d=0
op=''
for i in input:
    if i=='a':
        print(a)
    if i=='b':
        print(b)
    if i=='c':
        print(c)
    if i=='d':
        print(d)
    else:
        print()










    
    
