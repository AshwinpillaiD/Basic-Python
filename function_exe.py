#Exercise 1: Create a function in Python
'''
def profile(name,age):
    print('Name:',name,"\n","age:",age)

profile("ashwin",23)
  '''
#Exercise 2: Create a function with variable length of arguments 
'''
def var_len(*vl):
    print(vl)

var_len(1,2,3,4,4,5,6,54,34,2554,54,65,54,78)   
var_len(1,2,3,4,4,5,6,54,34,2554,54,65,54,78)   
'''
#Exercise 3: Return multiple values from a function
'''
def  cal(a,b):
    c=a+b
    d=a-b
    return c,d
cal1=cal(5,6)   
print(cal1)'''

#Exercise 3: Return multiple values from a function
'''
def add_sub(a,b):
    return a+b,a-b

add,sub=add_sub(3,5)
print(add,sub)
'''
#Exercise 6: Create a recursive function
