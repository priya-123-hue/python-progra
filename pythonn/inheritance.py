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

'''
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
'''

#multilevel inheritance
'''
class c1:
    a=10
    b=20
    c=30
class c2(c1):
    c=40
    d=50
    e=60
class c3(c2):
    e=70
    f=80
    g=90
print(c3.a)
print(c3.e)
print(c2.e)
'''
'''

class resume_10:
    size='a4'
    color='white'
    def __init__(self,name,dob,email,address,mark10,yop10):
        self.name=name
        self.dob=dob
        self.email=email
        self.address=address
        self.mark10=mark10
        self.yop10=yop10
    def display(self):
        print(self.name,self.dob,self.email,self.address,self.mark10,self.yop10,sep='\n')
    @classmethod
    def disp(cls):
        print(cls.color,cls.size)
class resume_12(resume_10):
    def __init__(self,name,dob,email,address,mark10,yop10,mark12,yop12):
        super().__init__(name,dob,email,address,mark10,yop10)
        self.mark12=mark12
        self.yop12=yop12
    def display(self):
        super().display()
        print(self.mark12,self.yop12,sep='\n')
class cse3(resume_12):
    def __init__(self,name,dob,email,address,mark10,yop10,mark12,yop12,cgpa,yop):
        super().__init__(name,dob,email,address,mark10,yop10,mark12,yop12)
        self.cgpa=cgpa
        self.yop=yop
    def display(self):
        super().display()
        print(self.cgpa,self.yop,sep='\n')
s1=cse3('priya','07-06-2007','priya13@gmail.com','chennaii',89.0,2022,92.0,2024,9.0,2028)
s1.display()
'''


#multiple inheritance
'''
class A:
    a=10
class B:
    a=20
class c(A,B): #c(B,A):
    pass

print(c.a)
'''

#ex2
'''
class A:
    a='snake'
    b='frog'
    c='cat'
class B:
    c='camel'
    d='dog'
    e='eagle'
class C(B,A):
    e='elephant'
print(c.e) 
'''
#add,sub
'''
class addition:
    def add(self):
        print(self.a+self.b)
class subtraction:
    def sub(self):
        print(self.a-self.b)
class calculator(addition,subtraction):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        ch=int(input('press \n1) for addition\n2) for subtraaction'))
        if ch==1:
          self.add()
        elif ch==2:
          self.sub()
        else:
          print("enter a valid no:")
op1=calculator(7,8)  

'''

#mul,div
'''
class multiply:
    def mul(self):
        print(self.a*self.b)
class division:
    def div(self):
        print(self.a/self.b)
class calculator(multiply,division):
    def __init__(self,a,b):
        self.a=int(input("enter a value1"))
        self.b=int(input("enter a value2"))
        ch=int(input('press \n1) for multiply\n2) for division'))
        if ch==1:
          self.mul()
        elif ch==2:
          self.div()
        else:
          print("enter a valid no:")
op1=calculator(5,25) 
''' 

#heirarchichal inheritance
#ex
'''
class A:
    a=10
class B(A):
    b=20
class C(A):
    b=30
print(C.a)
print(B.a)
print(C.b)
print(B.b)
'''

#multiple childclass,heirarchical inheritance
'''
class hotel:
    h_name = 'bilal'
    loc = 'velacherry'
    menu = {'spl.biriyani': 400, 'chicken biriyani': 350, 'mutton biriyani': 450}
    owner = 'MS Dhoni'

    def __init__(self, name, phno):
        self.name = name
        self.phno = phno

    def display(self):
        print(self.name, self.phno)

    @classmethod
    def show_menu(cls):  # Renamed from menu() to show_menu()
        for i in cls.menu.items():
            print(i)

    @classmethod
    def update(cls):
        iname = input("enter the name of the item: ")
        price = int(input('price of the item: '))
        cls.menu[iname] = price
        if iname in cls.menu:
            print("the price is updated")
        else:
            print('the item is added')
        print('the new price is:')
        cls.show_menu()  # Changed to call the renamed method

c1 = hotel('preethi', 6787645686885)
c1.show_menu()  # Changed to call the renamed method
c1.update()
'''

#using function
#create a function to print all the uperrcase character
'''
def up():
    for i in range(65,91):
        print(chr(i),end=' ')
up()
'''




#to print lower case character
'''
class lower:
   def low():
      for i in range(97,123):
         print(chr(i))
lower.low()
'''


# hybrid inheritance
# print uppercase,lc character,special.....

'''
class upper:
   @staticmethod
   def up():
      for i in range(65,91):
         print(chr(i),end=' ')
      print()
class lower:
   @staticmethod
   def low():
      for i in range(97,123):
         print(chr(i),end=' ')
      print()
class alphabet(upper,lower):
   pass
class digit:
   @staticmethod
   def dig():
      for i in range(0,90):
         print(i,end=' ')
class special:
   @staticmethod
   def spc():
      for i in '@#$%!&~':
         print(i)
class string(alphabet,digit,special):
   pass
upper.up()
lower.low()
digit.dig()
special.spc()
string.up()
alphabet.up()

'''

#multiple inheritance
'''
class basketball:
    b_ground_size=94*50
    b_team_size=7
class throwball:
    t_ground_size=48*73
    t_team_size=8
class volleyball:
    v_ground_size=76*33
    v_team_size=9
#class ground(basketball,throwball,volleyball): 
    #size=b_ground_size+t_ground_size+v_ground_size)
print(basketball.b_ground_size)
print(throwball.t_ground_size)
print(volleyball.v_ground_size)
'''
#same pgm can extend it..
'''

class basketball:
    b_ground_size=94*50
    b_team_size=7
class throwball:
    t_ground_size=48*73
    t_team_size=8
class volleyball:
    v_ground_size=76*33
    v_team_size=9
class ground(basketball,throwball,volleyball): 
    size= basketball.b_ground_size+throwball.t_ground_size+volleyball.v_ground_size
    team=basketball.b_team_size+throwball.t_team_size+volleyball.v_team_size
print(ground.size)
print(ground.team)
print(basketball.b_ground_size)
print(throwball.t_ground_size)
print(volleyball.v_ground_size)
'''
#priority
'''
class basketball:
    b_ground_size=94*50
    b_team_size=7
class throwball:
    t_ground_size=48*73
    team_size=8
class volleyball:
    v_ground_size=76*33
    v_team_size=9
class ground(throwball,volleyball,basketball): #based on priority it will display o/p
    size= basketball.b_ground_size+throwball.t_ground_size+volleyball.v_ground_size
    team=basketball.b_team_size+throwball.team_size+volleyball.v_team_size
print(ground.size)
print(ground.team)
print(ground.team_size)
'''


'''
class basketball:
    b_ground_size=94*50
    team_size=7
    @classmethod
    def display(cls):
        print(cls.b_ground_size)
        print(cls.team_size)
class throwball:
    t_ground_size=48*73
    team_size=8
class volleyball:
    v_ground_size=76*33
    v_team_size=9
class ground(throwball,volleyball,basketball): #based on priority it will display o/p
    size= basketball.b_ground_size+throwball.t_ground_size+volleyball.v_ground_size
    team=basketball.team_size+throwball.team_size+volleyball.v_team_size
    def __init__(self,name,height,age):
        self.name=name
        self.height=height
        self.age=age
print(ground.size)
print(ground.team)
print(ground.team_size)
player1=ground('priya',5.2,18)
player1.display()
'''








   





