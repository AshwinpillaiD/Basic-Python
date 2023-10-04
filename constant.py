'''
numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
  for y in items:
    print(x, y)
'''
'''
x = 0
while (x < 100):
  x+=2
print(x)'''   

'''
x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)'''

'''
print(0b101)
print(0o10)
print(0x1F)
'''
'''
import math
print(math.fabs(-45))
'''
'''
str1=["Welcome",2,4,6,7,8]
print(str1)
print(type(str1))
print(type(str1))


for i in str1:
    print([i],end="")
print("")'''
'''
str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count(sub,3)) # 3 define the index value
'''
'''
myString = ["pynative"]
stringList = ["abc", "pynative", "xyz"]
print(stringList[1] == myString)
print(stringList[1] is myString)'''

'''
myString = "pynative"
stringList = ("abc", "pynative", "xyz")

print(stringList[1] == myString)
print(stringList[1] is myString)
print(stringList[1] in myString)

'''
'''
class bike():
    print("welcome")
    b=10
    c=38

d=bike()
print(bike.b)
print(bike.d)
print(type(bike()))

'''
'''
a="ashwin"
def greet():
    #var="hello ashwin"
    var ="welcome"
    (globals()["a"])  #****global veriable calling syntax****(globles)
    #(globals()["a"])="changed" # how to global and globals variable also change syntax
    print(a)
greet()
print(a)    
'''
'''
def sum_numbers_from_list(number_list, target_number):
    # Initialize the sum
    total_sum = 0
    
    # Iterate through the list
    for num in number_list:
        if num <= target_number:
            total_sum += sum(range(1, num + 1))
    
    return total_sum

# Example usage:
my_list = [2, 4, 6, 8]
target_number = 6
result = sum_numbers_from_list(my_list, target_number)
print(f"The sum of numbers from 1 to {target_number} in the list is: {result}")
'''
'''
# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)
'''
'''
n = int(input("Enter number "))
# pass range of numbers to sum() function
x = list(range(1, n + 1))
print(sum(x))
print(type(x))
print('Sum is:', x)

'''
'''n=int(input("enter the value:"))
for i in range(2,n+1,2):
   
    print(i)'''
'''
n=int(input("enter the value:"))
for i in range(1,11):
    p = n*i
    print(p)


'''
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
       break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)
'''
'''
def custom_sum(values):
    sum_result = 0
    values_used = []  # To store the values used in the sum
    for value in values:
        sum_result += value
        values_used.append(value)
    return sum_result, values_used

# Define a list of values
values = [10, 20, 30, 40, 50]

# Calculate the sum and list the values used for the sum
result, values_used = custom_sum(values)

print("Values used for the sum:", values_used)
print("Sum:", result)

'''

class Student:
    # one argument constructor
    def __init__(self, name):
        print("One arguments constructor")
        self.name = name

    # two argument constructor
    def __init__(self, name, age):
        print("Two arguments constructor")
        self.name = name
        self.age = age

# creating first object
emma = Student('Emma',23)

# creating Second object
kelly = Student('Kelly', 13)



