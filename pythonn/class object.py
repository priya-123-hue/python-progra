'''class student:
    cname="panimalar"
    loc="chennai"
    def __init__(self,name,rollno):
       self.name=name
       self.rollno=rollno
    def display(self):
        print(self.name)
        print(self.rollno)
st1=student("priya",407)
st2=student("riya",408)
st1.display()
student.display(st1)'''

'''class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.14*self.radius*self.radius
shape1=circle(7)
print("area of circle",shape1.area())'''

'''class circle:
    def __init__(self,r):
       self.radius=r
    def circumference(self):
        return 2*3.14*self.radius
shape1=circle(3)
print("circum:",shape1.circumference())'''
'''
class shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def rectangle(self):
        return 2*(self.length+self.breadth)
    def square(self):
        return 4*self.length
s=shape(3,4)
print("area of rectangle",s.rectangle())
print("area of square",s.square())'''

#to modify
'''class student:
    cname="panimalar"
    loc="chennai"
    def __init__(self,name,rollno):
       self.name=name
       self.rollno=rollno
    def display(self):
        print(self.name)
        print(self.rollno)
    def ch_rollno(self,new):
        self.rollno=new
st1=student("priya",407)
st2=student("riya",408)
st1.display()
st2.ch_rollno(23)
student.display(st2)'''

'''class bank:
    bank_name="SBI"
    bank_manager="priya"
    branch="porur"
    ifsc='SBI0123456'
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
    
    @classmethod
    def display(cls):
        print(cls.bank_name,cls. bank_manager,cls.branch)
    @classmethod
    def ch_manager(cls):
       cls.bank_manager=input("enter the manager name:")
    
    
bank.display()
bank.ch_manager()
bank.display()'''


#static

'''            
class bank:
    bank_name="SBI"
    bank_manager="priya"
    branch="porur"
    ifsc='SBI0123456'
    def __init__(self,name,phno,email,pw):
        self.name=name
        self.phno=phno
        self.email=email
        self.pw=pw
    @staticmethod
    def valid_password(s):
        if len(s)<8:
            return False
        upper,lower,digit,special=0,0,0,0
        for i in s:
            if 'A'<= i <='Z':
                upper+=1
            elif 'a'<= i <='z':
                lower+=1
            elif '0'<= i <='9':
                digit+=1
            else:
                special+=1
        if upper>0 and lower>0 and digit>0 and special>0:
            return True
        else:
            return False
    def display1(self):
        
        if self.valid_password(self.pw):
            print("password is valid")
        else:
             print("password is not  valid")
    @staticmethod
    def valid_phno(s):
        if 6000000000<=s<=9999999999:
            return True
        else:
            return False
    def display2(self):
        if self.valid_phno(self.phno):
            print("phone no is valid")
        else:
             print("phone no is not  valid")
    
c1=bank('priya',909511923023,'priya12@gmail.com','Priya@38')
c1.display1()
c1.display2()
'''


#single inheritance
'''

class  shopping_mall:
    s_name="VR mall"
    loc='anna nagar'
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
    def display(self):
        print(self.name)
        print(self.phno)
    @classmethod
    def disp(cls):
        print(cls.s_name)
        print(cls.loc)
class shopping_mall_2(shopping_mall):
    loc2="padi"
    metro='koyambedu'
    def __init__(self,name,phno,email,pan):
        super().__init__(name,phno)
        self.email=email
        self.pan=pan
    def display(self):
        super().display()
        print(self.email)
        print(self.pan)
    @classmethod
    def disp(cls):
        super().disp()
c1=shopping_mall_2('priya',9094567839,'priya1@gmail.com',3425)
c1.disp()
c1.display()'''

#single inheritance2

'''class  shopping_mall:
    s_name="VR mall"
    loc='anna nagar'
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
    def display(self):
        print(self.name)
        print(self.phno)
    @classmethod
    def disp(cls):
        print(cls.s_name)
        print(cls.loc)
class shopping_mall_2(shopping_mall):
    loc2="padi"
    metro='koyambedu'
    def __init__(self,name,phno,email,pan):
        super().__init__(name,phno)
        self.email=email
        self.pan=pan
    def display(self):
        super().display()
        print(self.email)
        print(self.pan)
    @classmethod
    def disp(cls):
        super().disp()
c1=shopping_mall_2('priya',9094567839,'priya1@gmail.com',3425)
c1.disp()
c1.display()
c2=shopping_mall('riya',456372827388)
c2.disp()
c2.display()'''

#create a class called bank with class members (bname,branch)and 
#object member(name,addr,phno)
#then create a class called bank_update with class member(manager,facility)and 
#object member(pan,adhar,mail)
# create a  method to change phno and email
#single level inheritance


class bank:
    bname="sbi"
    branch="porur"
    def __init__(self,name,addr,phno):
        self.name=name
        self.addr=addr
        self.phno=phno
class bank_update:
    manager="ram"
    facility=["deposit",'account opening','withdraw','bank balance']
    def __init__(self,name,addr,phno,pan,adhar,mail):
        super().__init__(name,addr,phno)
        self.pan=pan
        self.adhar=adhar
        self.mail=mail
    def ch_ph(self):
        self.phno=input("enter the phno:")
    def ch_mail(self):
        self.mail=input("enter the new email:")
    @classmethod
    def new_facility(cls):
        new=input("enter new facility:")
        cls.facility+=[new]
c1=bank_update('anu','bangalore',67587433672,'hsjdh3645',34462728162,'anu1323@gmail.com')
print(bank_update.facility)
bank_update.new_facility()
print(bank_update.facility)

    








