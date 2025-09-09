#count the string
'''
def count():
  s='hello'
  c=0
  for i in s:
    c+=1
  print(c)
count()
'''
#abstract class : more than one abstract method
#concrete class:  class without one abstract method.


#calculator pgm using abstract method
'''

from abc import ABC,abstractmethod 
class calc(ABC):
    @abstractmethod
    def add():
        pass
    @abstractmethod
    def sub():
        pass
    @abstractmethod
    def mul():
        pass
    @abstractmethod
    def div():
        pass
class calculator(calc):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
ob1=calculator(10,20)
print(ob1.add())
print(ob1.sub())
print(ob1.mul())
print(ob1.div())
'''





    




