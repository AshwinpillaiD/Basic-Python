# type of exceptions in Python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

try:
    print(a)
except NameError as e:
    print("A is not Defined")
 
try:
    print(10 / 0)
except ZeroDivisionError :
    print("denominator cant be zero")
 
try:
    a = int("ashwin")
    #a = int(10)

except ValueError as e:
    print("Please Enter Numbers only")
 
try:
    a = [10, 20, 30, 40]
   # print(a[10])
    print(a[1])

except IndexError as e:
    print("Invalid Index")
 
try:
    f = open("app.py")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())
