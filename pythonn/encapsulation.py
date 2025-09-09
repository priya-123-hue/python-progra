
# encapsulation access specifier
'''
class phone:
    model='pro6' #public
    _phno=75849372637   #protected
    __password='priya12' #private
print(phone.model)
print(phone._phno)
print(phone.__password)'''


#fibonacci series of first 13 numbers 

''' n=13
a = 0
b = 0
c=1
for i in range(14):
    print(a)
    c = a + b
    a,b=b,c
    '''
#check whether the no is palindrome or not without slicing
'''
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
for i in range(13):
    print(fibo(i),end=' ')
    '''

#public access specifier(_)
'''
class company:
    cname='google'
    ceo='sundar pichai'
    head_quarters='california'
    _no_of_employee=180000  #protected
    _revenue=220000000 #protected
    def __init__(self,empid,empname,_sal):
        self.empid=empid
        self.empname=empname
        self._sal=_sal #private
    def display(self):
        print(self.empid,self.empname)   
    @classmethod
    def disp(cls):
        print(cls.cname,cls.ceo,cls.head_quarters) 
emp1=company('anu',5000,45367282)
emp2=company('priya',344527,6879000)
emp2.display()
emp2.disp()
print(emp1._revenue)
print(emp1._no_of_employee)
print(emp1._sal)
'''

#private(__)
'''
class company:
    cname='google'
    ceo='sundar pichai'
    head_quarters='california'
    _no_of_employee=180000  #protected
    __revenue=220000000 #protected
    def __init__(self,empid,empname,__sal):
        self.empid=empid
        self.empname=empname
        self.__sal=__sal #private
    def display(self):
        print(self.empid,self.empname)   
    @classmethod
    def disp(cls):
        print(cls.cname,cls.ceo,cls.head_quarters) 
emp1=company('anu',5000,45367282)
emp2=company('priya',344527,6879000)
emp2.display()
emp2.disp()
print(emp1.__revenue)
print(emp1._no_of_employee)
print(emp1.__sal)'''

#shortcut()
'''
class company:
    cname='google'
    ceo='sundar pichai'
    head_quarters='california'
    _no_of_employee=180000  #protected
    __revenue=220000000 #protected
    def __init__(self,empid,empname,_sal):
        self.empid=empid
        self.empname=empname
        self._sal=_sal 
    def display(self):
        print(self.empid,self.empname)   
    @classmethod
    def _private(cls):
        print(cls._no_of_employee,cls.__revenue) 
    def shortcut(self):
        print(self._sal)
        print(self.__revenue)
emp1=company('anu',5000,45367282)
emp2=company('priya',344527,6879000)
emp1.shortcut()
'''
#erro
'''
class company:
    cname='google'
    ceo='sundar pichai'
    head_quarters='california'
    _no_of_employee=180000  #protected
    __revenue=220000000 #protected
    def __init__(self,empid,empname,__sal):
        self.empid=empid
        self.empname=empname
        self.__sal=__sal #private
    def display(self):
        print(self.empid,self.empname)   
    @classmethod
    def _private(cls):
        print(cls._no_of_employee,cls.__revenue) 
    def __sal(self,new):
        self.__sal=new
emp1=company('anu',5000,45367282)
emp2=company('priya',344527,6879000)
emp1.display()
emp1._company_private()
'''

#class company for encapsulation
'''
class company:
    cname='Google'
    ceo='Sundar Pichai'
    head_quarters='California'
    _no_of_employees=183000
    __revenue=350000000
    def __init__(self,empid,empname,sal):
        self.empid=empid
        self.empname=empname
        self.__sal=sal
    def display(self):
        print('display method:')
        print('id:',self.empid,'name:',self.empname)
    @classmethod
    def disp(cls):
        print('class members:')
        print('company name:',cls.cname,'ceo:',cls.ceo,'head quarters:',cls.head_quarters)
    @classmethod
    def __private(cls):
        print('private method:')
        print('no of emloyees:',cls.no_of_employees,'revenue:',cls._revenue)
    def shortcut(self):#creating method to access private members outside the class
        print('Shortcut method to access private members:')
        print('emp id',emp1.empid)
        print('emp name',emp1.empname)
        print('salary:',emp1.__sal)
        print('company revenue:',emp1.__revenue)
    def __ch__sal(self):
        self.__sal=int(input('enter new salary:'))
    @classmethod
    def get_no_of_employees(cls):
        return(cls._no_of_employees)
    @classmethod
    def set_no_of_employees(cls,new):
        cls._no_of_employees=new
emp1=company(1,'Priyanka',100000)
emp1.disp()
emp1.display()
emp2=company(2,'Pri',150000)
emp2.display()
#emp1.shortcut()#calling hidden private properties 
#emp1.company_private()
#print('old salary:',emp1.company_sal)
#emp1.company_ch_sal()
#print('Updated salary:',emp1.company_sal)
#emp1.__private()

#getter and setter
print(company.get_no_of_employees())
company.set_no_of_employees(189067)
print(company.get_no_of_employees())
'''










    