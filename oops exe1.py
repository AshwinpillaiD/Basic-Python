'''
class person:
    def detail(self,name):
        print("the name is ",name)

    def detail1(self,name,age):
        print("the name is detail1",name,"\n",age)
class family(person):
    def details(self):
        person.detail(self,"ashwin")
        super().detail1("ashwoin",23)
obj=family()
obj.details()

''''''
class ashwin:
    def ashwin1(self):
        print("ashwin")
class raj:
    def ashwin2(self):
        print("raj")

class shyam(ashwin,raj):
    def shyam1(self):
        super().ashwin2()
        super().ashwin1()
        print("shyam")


obj=shyam()
obj.shyam1()        

'''
'''
class a:
    def __init__(self):
        print("contrutor_class A")

    def method(self):
        print("printing from class")
class b(a):
    def __init__(self):
        print("contrutor_class b")
        super().__init__()

    def method(self):
        print("printing from class")
        super().method()

class c(b):
    def __init__(self):
        print("contrutor_class b")
        super().__init__()

    def method(self):
        print("printing from class")
        super().method()

obj=c()
obj.method()
'''
'''
class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

class rectangle(shape):
    def __init__(self,length,breadth):
       super().__init__(length,breadth)
       print("rectangle:",self.length*self.breadth)

class cube(shape):
    def __init__(self,length,breadth,height):
       super().__init__(length,breadth)
       print("cube",length*breadth*height)
r=rectangle(7,8)        
c=cube(4,5,6)

'''
"""


sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)
"""
'''
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
a=len(sample_list)//3
print(a)
'''
'''
class chadura:
    def method2(self,name="ashwin"):
        print("Name:"+name)
class chadura1(chadura):
    def method(self,name="shyam"):
        super().method2()
        print("NAME:",name)
        
#emp1=chadura()
emp2=chadura1()
emp2.method()

''''''
a=10
b=49.0
print(a+b)

'''
'''
try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError as e:
    print(e)  
'''
'''
try:
    a=24
    b=47
    int.__add__(a,b)
    print(a+b)
except TypeError as e:
    print(e)

'''
'''
class stundent:
    def __init__(self,m1,m2):
        
            self.m1=m1
            self.m2=m2
            
s1=stundent(3,4)
s2=stundent(5,3)

'''
'''
class student:
    def __init__(self,mark1,mark2):
        self.m1=mark1
        self.m2=mark2
    def __add__(self,temp):
        first_stu=self.m1+ self.m2
        second_stu=temp.
'''
'''
a=10
b=37
int.__add__(a,b)       '''

'''
a="ash"
b="win"
c="pillai"
print(str.__add__(a,b))
'''
'''
class student:
    def __init__(self,mark1,mark2):
        self.m1=mark1
        self.m2=mark2

    def __add__(self,temp):
        first_stu=self.m1+self.m2
        second_stu=temp.m1+temp.m2
        print("ashwin")
        total=student(first_stu,second_stu) 
        return total

  #  def __sub__(self,temp):
  #      first_stu=self.m1+self.m2
  #      second_stu=temp.m1+temp.m2
  #      total=student(first_stu,second_stu) 
  #      return total    


s1=student(20,40)
s2=student(30,50)
#total=s1-s2
total=s1+s2
'''
#print(total.m1)
#print(total.m2)


'''
class ashwin:
    def __add__(a,b):

        print("hai chadura")

s1=ashwin()
s1.__add__(2,3)
s2=ashwin()
s2.__add__(5,7)
total=s1+s2

'''



