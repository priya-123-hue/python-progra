# add the numbers
'''
def add(a,b):
    print(a+b)
def add(a,b,c):
    print(a+b+c)
def add(a,b,c,d):
    print(a+b+c+d)
add(3,2,2,3)
#if give add(2,3)error(overiding)
'''

 #[function-outside the class]monkey batching(storing the address of the function )(taking two container)
'''
def add(a,b):
    print(a+b)
s=add
def add(a,b,c):
    print(a+b+c)
t=add
def add(a,b,c,d):
    print(a+b+c+d)
s(5,5)
t(1,1,1)
add(3,2,2,3)
'''

#[method-inside the class]
'''
def add(a,b):
    print(a+b)
s=add
def add(a,b,c):
    print(a+b+c)
t=add
def add(a,b,c,d):
    print(a+b+c+d)
s(5,5)
t(1,1,1)
add(3,2,2,3)
class demo:
    @staticmethod
    def sample():
        print('lab6 is super')
    l=sample
    @staticmethod
    def sample(n):
        if n<=1:
            print('not a prime')
            return 
        for i in range(2,n):
            if n%i==0:
                print("not a prime")
            else:
                print('prime')
demo.l()  #monkey patch
demo.sample(1)
'''

#operator overloading()
#magic methods (__,)

'''
a=10
print(type(a))
class arithmetic:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a/other.a #operator overloading(*,+,-)
ob1=arithmetic(10)
ob2=arithmetic(20)
#print(type(ob1))  #<class '__main__.arithmetic'>
print(ob1+ob2)
'''

#using def__add__
'''

a=10
print(type(a))
class arithmetic:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a #operator overloading(*,+,-)
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self,other):
        return self.a*other.a
    def __floordiv__(self,other):
        return self.a//other.a
    def __truediv__(self,other):
        return self.a/other.a
    def __mod__(self,other):
        return self.a%other.a
ob1=arithmetic(10)
ob2=arithmetic(20)
#print(type(ob1))  #<class '__main__.arithmetic'>
print(ob1+ob2)
print(ob1-ob2)
print(ob1*ob2)
print(ob1//ob2)
print(ob1/ob2)
print(ob1%ob2)
'''

#method overriding
'''

def sample():
    print('for memory allocation')
temp1=sample
def sample(a,b):
    print(a*b)
temp2=sample  #mb
def sample(a,b,c):
    print(a+b+c)
temp1()
temp2(4,4)
sample(1,1,1)
'''

















