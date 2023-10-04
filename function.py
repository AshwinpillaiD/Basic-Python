
# funtion statement
'''
def ashwin():
     print('hello word') 

ashwin()

'''
'''
# No Return Type Without Argument Function in Python
def add():
    a=int(input("enter the value a:"))
    b=int(input("enter the value b:"))
    c=a+b 
    print(c)
add()   
'''


# No Return Type With Argument Function in Python
'''

def sub(a,b):   # with argument
    c=a-b
    print(c)
    
a=int(input("enter the value a:"))
b=int(input("enter the value b:"))
sub(a,b)

'''
'''
#  Return Type Without Argument Function in Python

def multi():
    a=int(input("enter the value a:"))
    b=int(input("enter the value b:"))
    c=a*b
    print(c)

x=multi()
print(x+21)

'''
'''
#  Return Type With Argument Function in Python

def div(a,b):   # with argument
    c=a/b
    print(c)
    return c
    
a=int(input("enter the value a:"))
b=int(input("enter the value b:"))
x=div(a,b)
div(a,b)

'''
# Arbitrary Arguments Function in python(*)
'''
def std_id(*std):
    print(std)
    print()
    for num in std:
        print(num)

std_id("ashwin","shyam","raj")


 # keyword arguments funtion in python
'''
'''
def frt_last(name,last):
    print(name,"last is",last)

frt_last(name="ashwin",last="pillai")
'''
'''
 # Arbitrary keyword arguments in python
def bio_data(**data):
    return data

x=bio_data(name="ash", na="www",jifmj=77,jmdnd="kskfsdio-jkfds")     
print(x)

'''
# Default Parameter Function in Python
'''
def user(name,place="klt"):
    print(name,"is from",place)

user("ashwin","karur")
user("ashwin")

'''

# Passing a List as an Argument in Function Python
'''

def total(marks):
    return sum(marks)
 
print("Total : ",total([55, 75, 80, 95, 47]))

  
'''  
# recursive funtion
'''
def factorial(x):
  #  pass
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))

print("factorial:",factorial(3))
'''
'''
# lambda funtion
a=lambda a:a+70
print(a(5))

a=lambda a,b:a*b
print(a(3,5))
'''

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a + n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
