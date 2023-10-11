'''
class Bike:
    def hero(self, a,b): 
        self.a=4
        self.b=6
        return self.a,self.b                # self argument used to give the one fuction input to access the all function 
        print("good mileage bike")

    def R15(self):
        self.a 
        self.b 
        print("hai", self.a,self.b)
        
b=Bike()
b.hero(2,4)
b.R15()
print(b.hero(2,4))
'''
'''
class Bike:
    def hero(self, name): 
        self.name = name                  # Self argument used to give the one function input to access the all function 
      #  print("good mileage bike")

    def R15(self):
        print(self.name)

a=Bike()
a.hero("Ashwin")
a.R15()'''

# construtor oops
'''
class house():
    def __init__(self,company,ceo):
        self.company=company
        self.ceo=ceo
        a=10
        print(company,ceo)
    def r15(self,name,year):
       
        print(name)
        print(year)            
    def duck(self,model,year):
        
        print(year)

obj=house('chadura','kumaran')
obj1=house("Ashwin",'Ashwin')
obj1.r15(name="bike",year=2)
obj.duck(123,20202)
obj.__init__("Ashwin","ashw")


'''

#Recursive
'''
i=0
def greeting():
    global i
    i+=1
    print("hai Ashwin",i)
    greeting()
greeting()

'''
'''
import sys
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit()) 

i=0
def greeting():
    global i
    i+=1
    print("hai Ashwin",i)
    greeting()
greeting()

'''
# self parameter
'''
class school():
    Place="klt"
    def std(self,name,id):
       # self.Place
        print("name:",name)
        print("id:",id)
        global Place
        Place='karur'
        print("place:",Place)

obj=school()
obj.std("Ashwin",54)

'''
'''
class person:
    def get_detils(self,name,age):
        self.name=name
        self.age=age
    def print_detils(self):
        print("name",self.name)
        print("name",self.age)

a=person()
a.get_detils("Ashwin",23)
a.print_detils()
print(a)

'''
'''
class room:
    def cal(self):
        length= 0.0
        breath= 0.0
        print('area',room1.length*room1.breath)

room1=room()
room1.length=23.5
room1.breath=645.7

room1.cal()
print("------------------------------------------")
class room:
    def cal(self):
        length= 0.0
        breath= 0.0
        print('area',self.length*self.breath)

room1=room()
room1.length=23.5
room1.breath=645.7

room1.cal()

'''
# non parameterized contructor
'''
class  ems:
    def __init__(self):
        self.name="Ashwin"
        self.age=23  

    def show(self):
        print("name",self.name)
        print("age",self.age)

emp1=ems()
emp1.show()

'''
# parameterized contructor
'''
class chadura_ems:
    def __init__(self,name,age):
       self.name=name
       self.age=age
       print(name,"\n",age)
emp1=chadura_ems("Ashwin",23)

'''

'''
class chadura_ems:
    a=19
    def __init__(self,name,age=19):
       self.name=name
       self.age=age 
       
    def show(self):
        print("name",self.name)
        print("age",self.age)

emp1=chadura_ems("Ashwin",23)
emp1.show()'''
'''
class chadura_ems:
    a=19
    def __init__(self,name,age=19):
       self.n=name
       self.a=age 
       
    def show(self):
        print("name",self.n)
        print("age",self.a)

emp1=chadura_ems("Ashwin",23)
emp1.show() 
emp2=chadura_ems("raj",23)
emp2.show() 
emp3=chadura_ems("shyam",23)
emp3.show() 
emp3=chadura_ems("saran",23)
emp3.show()      

'''
'''
class chadura:
    z=0
    def __init__(self,x,*y):
        z=x
        for i in y:
            z+=i
        print(z)
   
obj=chadura(10,20,30,40,50,60,70)
'''
'''
class person:
    def __init__(self,name,**values):
        print(name)
        print(values['age'])

obj=person("Ashwin",age=45)

'''
'''
class Ashwin:
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def ashw(self):
        self.area=self.b*self.h*0.5
        print(self.area)

obj=Ashwin(4,5)
obj.ashw()

'''
'''
class chadura:
    def __init__(self):
        print("obj created")
    def __del__():
        print("obj deleted")
emp1=chadura()
print(emp1)
'''
'''

class person:
    def __init__(self,a,b) :
        c=a+b
        return None
        print("Ashwin")
__new__=person(2,6)
   '''     
     

'''      
class Student:
    # constructor with default values age and classroom
    def __init__(self, name, age, classroom=7):
        self.name = name
        self.age = age
        self.classroom = classroom

    # display Student
    def show(self):
        print(self.name, self.age, self.classroom)

# creating object of the Student class
emma = Student('karthi','Ashwin')
emma.show()

kelly = Student('Kelly', 13)
kelly.show()

'''
#
#class person:
#    def __init__(self,a,b) :
#        c=a+b
#        return None
#        print("Ashwin")
#__new__=person(2,6)
''''        
class Student:
    # constructor with default values age and classroom
    def raj(self, name, age=12, classroom=7):
        self.name = name
        self.age = age
        self.classroom = classroom

    # display Student
    def show(self):
        print(self.name, self.age, self.classroom)

# creating object of the Student class
emma = Student()
emma.raj("Ashwin")
emma.show()

'''
'''
class Student:
    # one argument constructor
    def __init__(self, name):
        print("One arguments constructor")
        self.name = name

    # two argument constructor
    def __init__(self, name, age):
        print("Two arguments constructor")
      #  self.name = name
       # self.age = age

# creating first object
emma = Student('Emma')

# creating Second object
kelly = Student('Kelly', 13)

 
''''''
class famliy:
    # Constructor of Vehicle
    def __init__(self, thattha,pati):
        print('first genarasen')
        self.thattha,pati = thattha,pati

class gen1(famliy):
    # Constructor of Car
    def __init__(self,thattha,pati,appa,amma):
        super().__init__(thattha,pati)
        print('Inside Car Constructor')
        self. appa,amma=appa,amma
class gen2(gen1):
    # Constructor of Electric Car
    def __init__(self,thattha,pati,appa,amma,son,daughter):
        super().__init__(thattha,pati,appa,amma)
        print('Inside Electric Car Constructor')
        self.son,daughter=son,daughter

# Object of electric car
ev = gen2('sathasivan-arumugam','angamal-dhanam','devendran',"valliyamma","Ashwin",'anith_vasanthi')
print(f'Thattha={ev.thattha}, appa={ev.appa},son={ev.son}')
'''
'''
class Employee:
    count = 0
    def __init__(self):
        Employee.count = Employee.count + 1
e1 = Employee()
e2 = Employee()
e2 = Employee()
print("The number of Employee:", Employee.count)'''
'''
class founder:
    def __init__(self,foun_name):
        self.foun_name=foun_name
        print("the founder",self.foun_name)
    
class voice_pre(founder):
    def __init__(self,foun_name,voice_name):
        super().__init__(foun_name)
        self.voice_name=voice_name
        print(self.voice_name,self.foun_name)

class tech(voice_pre):
    def __init__(self, foun_name, voice_name,tech_name):
        super().__init__(foun_name, voice_name)
        self.tech_name=tech_name
        print(self.voice_name,self.foun_name,self.tech_name)

chadura=tech('gnanavel','kumarean','xyz')      
 '''

'''
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

'''
'''
def outer (a,b):
    suqare=a**2
    def add(a,b):
        return a+b
    addi=add(a,b)
    return addi+5

result=outer(5,10)
print(result)
'''
'''

def  recursive(num):
    if num:
        return num+recursive(num-1)

    else:
        return 0
res= recursive(10)
print(res)
'''
'''
def display_std(name,age):
    print(name,"\n",age,sep="***")

show_tu=display_std

show_tu("Ashwin",23)
'''
'''
a=[]
for i in range(4,30):
    if i%2==0:
        a.append(i)
print(a)'''
'''
a=[]
for i in range(4,30,2):
    a.append(i)
print(a)'''
'''
print(list(range(4,30,2)))
''''''
a=[4,6,8,24,12,2]
print(max(a))'''

'''
str="ash2win"
print(str[len(str)//2])


print("first:",str[0],"\n","last:",str[-1])'''
'''

def extract_characters(input_string,middle_character=" "):
    if len(input_string) < 3:
        return "Input string should have at least 3 characters"
    
    
    if input_string[len(input_string) // 2]==2:

        middle_character = input_string[len(input_string) // 2]
    else:
        print('Not middle_character')
    first_character = input_string[0]       
    last_character = input_string[-1]
    
    return f"{first_character}{middle_character}{last_character}"

input_string = input("Enter a string: ")
result = extract_characters(input_string)
print(f"Result: {result}")

'''
#Exercise 1B: Create a string made of the middle three characters
'''
input_string=input("enter the string:")
a=len(input_string)//2
   
middle=input_string[a]
rmiddle=input_string[a-1]
lmiddle=" "

   
print(f"{rmiddle}{middle}{lmiddle}")
print(a)

input_string[2]
'''


'''x
input_string=input("enter the string:")
a=(len(input_string)//2)+1
b=len(input_string)
if b%2==0:
    middle=input_string[a-1]
    rmiddle=input_string[a-2]
    lmiddle=" "
else:
     middle=input_string[a-1]
     rmiddle=input_string[a-2]
     lmiddle=input_string[a]

   
print(f"{rmiddle}{middle}{lmiddle}")
print(a)

input_string[2]

 ''''''
def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("ashwin")
get_middle_three_chars("JaSonAy")

''''''
a="ashwin"
b="pillai"
middle=len(a)//2
firt=a[:middle]
second=a[middle:]

print("{}{}{}".format(firt,b,second))


'''
'''
str="nsvhgHHVHjJGuV@47%75*Gyf75"
print(len(str))
char=0
digits=0
symbol=0
for iteam in str:
    if iteam.isalpha():
        char=char+1
    elif iteam.isdigit():
        digits=digits+1
    else:
        symbol=symbol+1
print(char,"\n",digits,"\n",symbol)

''''''
s1="ash"
s2="ashwin"
print(s1 in s2)
'''
'''
item="gdfk28763bhdgc#%$63"
for i in item:
    if i.isdigit:
       item[i]+=item[i]
    print(i)

'''
'''
import re

input_str = "PYnative29@#8496"
digit_list = [int(num) for num in re.findall(r'\d', input_str)]
print('Digits:', digit_list)

# use the built-in function sum
total = sum(digit_list)

# average = sum / count of digits
avg = total / len(digit_list)
print("Sum is:", total, "Average is ", avg)

''''''
str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)
'''
'''
tr1 =" Emma-is-a-data-scientist"
print(tr1.split("-"),"\n")

'''
'''
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

str=list(filter(None,str_list))
print(str)

'''
'''
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

a=len(l1)
b=len(l2)
olist=[]
elist=[]
for i in range(1,a,2):
    olist.append(l1[i])
print(olist)
for j in range(0,a,2):
    elist.append(l2[j])
print(elist)

'''
# sigle level inheritance
'''
class parent():
    def parent1(self,name="ashwin",age=23,place='klt'):
        print("emp name:",name)
        print("emp age:",age)
        print("emp place:",place)

class child(parent):
    def child1(self,pin=639107):
        print("pin:",pin)
        
obj=child()
obj.parent1()
obj.child1()
'''
#multilevel inheritance
'''
class parent:
    def personal(self,name="ashwin",age=23,gender='M'):
        print('name:{}\nage:{}\ngender:{}'.format(name,age,gender))
class child1(parent):
    def company(self,name="chadura",location="musiri"):
        print('c.name:{}\nc.loc:{}'.format(name,location))
class child2(child1):
    def other(self,salary=15000,designation="inten"):
        print('saraly:{}\ndesignation:{}'.format(salary,designation))

obj=child2()
obj.personal()
obj.company()
obj.other()      

'''
'''
class parent:
    def personal(self,name="ashwin",age=23,gender='M'):
        print('name:{}\nage:{}\ngender:{}'.format(name,age,gender),"\n")
class child1():
    def company(self,name="chadura",location="musiri"):
        print('c.name:{}\nc.loc:{}'.format(name,location),"\n")
class child2():
    def other(self,salary=150000000,designation="inten"):
        print('saraly:{}\ndesignation:{}'.format(salary,designation),"\n")
class child3(child2,child1,parent):
    def ashwin_don(self):
        print("hai")


obj=child3()
obj.personal()
obj.company()
obj.other()  
'''
'''
class chadura:
    def chadura_team(self):
        print('hello team')

class founder1(chadura):
    def founder(self):
        print("the founder gnanavel")

class voice(chadura):
    def voice1(self):
        print("the voice precedent kumaran")

class tech(chadura):
    def tech1(self):
        print("the tech baskeran")

obj1=founder1()
obj1.chadura_team()
obj1.founder()

obj2=voice()
obj2.chadura_team()
obj2.voice1()

obj3=tech()
obj3.chadura_team()
obj3.tech1()

'''
#hybird inheritance
'''
class family:
    def parent(self,mother="valli",father=None):
        print(father,mother)
class akka1():
    def  akka_f1(self,akk1=None,mama1=None):
        print(akk1,mama1)
class akka2(family):  
    def akka_f2(self,akk2=None,mama2=None):
        print(akk2,mama2)
class bro(akka2,akka1):
    def bro_f1(self,name=None):
            print("ashwin")
obj3=bro()
obj3.bro_f1()
obj3.parent()

obj3.akka_f1()
obj3.akka_f2()

'''
# constructor and inheritance
'''
class a:
    def __init__(self):
        self.name="ashwin"

        print("i am a init:"+self.name)
    def emp(self):
        print("i am funt 1")
class b(a):
    def emp2(self):
        print("i am emp2"+self.name)

obj=b()
#obj.emp()
obj.emp2()

'''
'''
class a:
    def __init__(self):
        print(" hai aswhin")
    def func1(self):
        print("hello raj")

class b(a):
    def __init__(self):
        print("function2")
        super().__init__()
        print("super method")
    def fun2(a):
        print("func_2 complete ")        

obj=b()
print(b.mro())
'''
'''
class stu:
    def __init__(self,value):
        self.value=value
    def __gt__(s,other):
        if (s.value > other.value):
            return True
        else:
            return False
obj=stu(7)
obj1=stu(4)
if (obj>obj1):
    print("obj greater than obj1")
else:
    print("obj1 greater than obj2")
'''
'''
class stu:
    def __init__(self,value):
        self.value=value
    def __gt__(s,other):
        if (s.value > other.value):
            print("obj greater than obj1")
        else:
            print("obj1 greater than obj")

obj=stu(2)
obj1=stu(4)
obj>obj1
'''
'''
class stu:
    def __init__(self,value=45):
        self.value=value
    def __ge__(s,other):
        if (s.value >= other.value):
            print("obj greater than or equal obj1")
        else:
            print("obj1 greater than obj")

obj=stu()
obj1=stu()
obj>=obj1
'''
'''
class ashwin:
    def fun(self,a):
        print(a)
    def fun(self,a,b):
        print(a+b)
    def fun(self,a,b,c):
        print(a+b+c)
   
a=ashwin()
a.fun(4,5,6)
'''
'''
class ashwin:
    def fun(self,a=None):
        print(a)
    def fun(self,a,b):
        print(a+b)
    def fun(self,a,b,c):
        print(a+b+c)
   
a=ashwin()
a.fun(4,5,6)'''
'''
class a:
    def fun(self,a=None,b=None,c=None):
        if (a!=None and b!=None and c!=None):
            print(a+b+c)
        elif(a!=None and b!=None):
            print(a+b)
        else:
            print(a)
obj=a()
obj.fun(23,65)

obj.fun(23)
obj.fun(23,65,43)
'''
# method overloding using multiple dispatch
from multipledispatch import dispatch
'''
@dispatch(int,int)
def add(a,b):
    return a+b

@dispatch(int,int,int)
def add(a,b,c):
    return a+b+c  

print(add(3,4))
print(add(10,30,45))

'''
'''
@dispatch(float,int)  #" ****** "
def add(a,b):
    return a+b

@dispatch(int,float,int)
def add(a,b,c):
    return a+b+c 

@dispatch(int,float,str)
def add(a,b,c):
    return a+b,c 

#print(add(3,4))       " exception error :-not implemented error"
print(add(10,30.3,"ashwin"))

'''
'''
class a:
    def detail(self):
        print("i am from in class a")
class b(a):
    def detail(self):
        print("i am from in class b")
class c(b):
    def detail(self):
        print("i am from in class c")

obj=c()
obj.detail()
'''
'''
# polymarphism using inhertance
class a:
    def detail(self,name="chadura"):
        print("hai",name)

class b(a):
    def detail(self):
        super().detail(name="chadura")
        print("hello")

obj=b()
obj.detail()

'''
# method overriding
# Using multiple inheritance
'''
class a:
    def detail(self):
        print("i am from class a")

class b():
    def detail(self):
        super().detail()
        print("i am from class b")

class c():
    def detail(self,*value):
        super().detail()
        print("i am from class c",value)

class d(c,b,a):
    def detail(self):
        super().detail()
        print("i am from class d")

obj=d()
obj.detail()
'''
'''

class c():
    def detail(self,**value):   # u give the empty keyword arrument the output well be {}
        print("i am from class c",value)
obj=c()
obj.detail()
'''
'''
class ashwin:
    def speak(self):
        return "i am ashwin"
class shyam:
    def speak(self):
        return "i am shyam"

class raj:
    def speak(self):
        return "i am raj"

obj1=ashwin()
obj2=shyam()
obj3=raj()
       
for i in (obj1,obj2,obj3):
    print(i.speak())

'''
'''
class ashwin:
    def speak(self):
        return "i am ashwin"
class shyam:
    def speak(self):
        return "i am shyam"

class raj:
    def speak(self):
        return "i am raj"

obj1=ashwin(),shyam(),raj()
       
for i in (obj1):
    print(i.speak())
'''
'''

class vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def show(self):
        print("details",self.name,self.color,self.price)
    def speed(self):
        print("vehicle max speed is 100")
    def gear(self):
        print("scooty -no gear")

class car(vehicle):
    def speed(self):
         print("car max speed is 240")
    def gear(self):
        print("car max speed is gear")

car=car("kwid","red","4l")
car.show()
car.speed()
car.gear()

print("\n")

vehicle=vehicle("scooty","blue","10l")
car.show()
car.speed()
car.gear()

'''
'''
class vehicle():
    def car1(self,name,color,price,gear="yes",speed=240):
        print("Name:{} \n color:{}\n price:{}".format(name,color,price))
        print(f"Gear:{gear}\n speed:{speed}")
class scooty(vehicle):     
    def scooty1(self,name,color,price,gear="No",speed=100):
        print("Name:{} \n color:{}\n price:{}".format(name,color,price))
        print(f"Gear:{gear}\n speed:{speed}")

obj=scooty()
obj.car1('kwid','blue',10000)
print("\n")
obj.scooty1("scooty","yellow",30000)

'''
# Encapsulation 
'''
class test:
    def detail(self,name,age):
        self.name=name
        self.age=age

obj=test()
obj.detail("ashwin",23)  #*******
print("name:",obj.name)
print("name:",obj.age)


class test:
    def detail(self,name,age):
        self.name=name
        self.age=age
obj=test()
obj.detail("ashwin",23)
obj.name="appu"          # encapsulation  data not serure well be change (name)
print("name:",obj.name)
print("name:",obj.age)

'''
# Encapsulation using public variable method
'''class chadura:
    def detail(self,name,age):
        self.name=name
        self.age=age
        print("Name:",self.name)
        print("Name:",self.age)

emp1=chadura()
emp1.detail("ashwin",23)
print("Name:",emp1.name)
print("Name:",emp1.age)

'''
'''

class chadura:
    def detail(self,name,age):
        self.name=name
        self.age=age
    print("Name:",emp1.name)  # error  NameError=name 'emp1' is not defined

    print("Name:",emp1.age)

emp1=chadura()
emp1.detail("ashwin",23)
'''

#  Encapsulation using private variable
'''
class chadura:
    def detail(self,name,age):
        self.__name=name
        self.__age=age
        print("Name:",self.__name)
        print("age",emp.__age)

emp=chadura()
emp.detail("ashwin",23)

print("age",emp.age) # attribute error

'''
'''
class chadura:
    def detail(self,name,age):
        self.__name=name
        self.__age=age
        print("Name:",emp.__name)
        print("age",emp.__age)

emp=chadura()
emp.detail("shyam",23)

class chadura:
    def detail(self,name,age):
        self.__name=name
        self.__age=age
    print("Name:",emp.__name)
    print("age",emp.__age)

emp=chadura()
emp.detail("ashwin",23)

'''
# private variable using public variable
'''
class chadura:
    def detail(self,name,age):
        self.__name=name  # private variable using public variable
        self.age=age      # public variable
        print("Name:",emp.__name)

    def show(self):
        print("Name:",emp.__name)
        print("age",emp.age) # public variable
emp=chadura()
emp.detail("shyam",23)
emp.show()
print("age",emp.age)     # public variable

'''
# private method call using public method 
'''
class school:
    def detail(self):
        self.name="asggwdfb"
        print("school name",self.name)
    def __stu1(self):
        print("name: ashwin")
        print("class: 10th")
        print('\n')
    def stu2(self):
        self.__stu1()
        print("name: ash")
        print("class: 11th")
obj=school()
obj.detail()
obj.stu2()
'''
'''  
class school:
    def detail(self):
        self.name="asggwdfb"
        print("school name",self.name)
    def __stu1(self):
        print("name: ashwin")
        print("class: 10th")      
    def __stu2(self):       
        print("name: ash")
        print("class: 11th")
obj=school()
obj.detail()
obj._school__stu1()
obj._school__stu2()
'''
"""
class detail:
    _name="ashwin"
    _roll=3645476
    def display(self):
        print("Name",self._name)
        print("Roll no",self._roll)
    
obj=detail()
obj.display()
"""
'''
class base:
    def __init__(self):
        self._name="ashwin"
class derived(base):
    def __init__(self):
     #   super().__init__()
        base.__init__(self)
        print("calling from the derived class",self._name)
        self._name="Shyam"
        print("modified name",self._name)

obj1=derived()
obj2=base()
print("Accessing protected member of obj1:",obj1._name)
print("Accessing protected member of obj2:",obj2._name)

'''
# setter and getter concept
'''
class detail:
    def setname(self,n):
        self.__name=n
    def getname(self):
        return self.__name
    def display(self):
        print("student name :",self.__name)

obj=detail()
obj.setname("ashwin")
obj.display()
'''
'''
class detail:
    def setname(self,n):
        self.__name=n
    def getname(self):
        return self.__name

    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age

    def display(self):
        print("student name :",obj.getname())
        print("student age :",self.__age)

obj=detail()
obj.setname("ashwin")
obj.setage(23)
obj.display()

'''
'''
class chadura:
    def __init__(self):
        self._age=0
    
    @property
    def age(self):
        print("getter method called")
        return self._age
    
    @age.setter
    def age(self,n):
        if n<18:
            print("age is below 18")
        print("call the setter method")
        self._age =n

obj=chadura()
obj.age = 10
print(obj.age)
obj.age = 0
print(obj.age)
obj.age = 19
print(obj.age)
        
'''

























