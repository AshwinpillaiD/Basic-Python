# Exercise 1: Accept numbers from a user(Write a program to accept two numbers from the user and calculate multiplication)
'''
a=int(input('enter the value A:'))
b=int(input('Enter the value B:'))
c=a*b
print(c)

def multi():
    a=int(input('enter the value A:'))
    b=int(input('Enter the value B:'))
    c=a*b
    return c
    
x=multi()
print(x)
'''
#Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
'''

str=("Name",'Is',"james")
print(type(str))
a="**".join(str)
print(a)

print(str[0],"**",str[1],"**",str[2])


print('My', 'Name', 'Is', 'James', sep='**')  #@\\\\\\\\\\\\\\\\//////////
'''
#Exercise 3: Convert Decimal number to octal using print() output formatting
'''
a=8
oc=oct(a)
print(oc)
b=2133.8764
print("%.2f"% b)
'''
#Exercise 4: Display float number with 2 decimal places using print()
'''
num= 2324.541767564
rounded_number = round(num,3)
print(rounded_number)

num = 458.541315
print('%.2f' % num)
num1={:.2f}".format(num)
print(num1)
'''
#Exercise 5: Accept a list of 5 float numbers as an input from the user
'''a=[]
for i in range(0,5):
    b=float(input("Enter the value:"))
    a.append(b)
    print(a)

# Initialize an empty list to store the float numbers
float_numbers = []'''

# Use a loop to get 5 float numbers from the user
'''
float_numbers = []
for i in range(5):
    while True:
        try:
            # Get user input and convert it to a float
            num = float(input(f"Enter float number {i + 1}: "))
            float_numbers.append(num)
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Invalid input. Please enter a valid float number.")

# Display the list of float numbers
print("List of float numbers:", float_numbers)
'''
#Exercise 7: Accept any three string from one input() call
'''
name1,name2,name3=input("enter the three value:").split( )
print("name1",name1)
print("name2",name2)
print("name3" ,name3)
'''

#Exercise 8: Format variables using a string.format() method.
'''
totalMoney = 1000 #{0}
quantity = 3 #{1}
price = 450 #{2}
#enter the index value fixed  {1},other wise index consider as {0}
# only opperate automatical or manuel
stringformat="I have {} dollars so I can buy {} football for {} dollars."
print(stringformat.format(totalMoney,quantity,price))
'''
#




