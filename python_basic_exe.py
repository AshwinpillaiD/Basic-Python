#Calculate the multiplication and sum of two numbers
'''
num1=int(input("enter the value num1:"))
num2=int(input("enter the value num2:"))
c=num1*num2
#print("the result is",c)
if c<=1000:
    print("the result is",c)
else:
   # num1=int(input("enter the value a1:"))
   # num2=int(input("enter the value a2:"))
    d=num1+num2
    print("the result is",d)


def mul_or_add(num1,num2):
    c=num1*num2
    if c<=1000:
        return c
    else:
        c=num1+num2
        return  c      
print("the result is",mul_or_add(20,30))
print("the result is",mul_or_add(40,30))
print("-------------------------------------------------")
'''
 #Print the sum of the current number and the previous number
'''
previous_num=0
for current_number in range(1,11):
    x_sum = previous_num +current_number
    print("Current Number",current_number , "Previous Number ", previous_num, " Sum: ", x_sum)
    previous_num+=1
print("-------------------------------------------------")
'''
#Print characters from a string that are present at an even index number
'''
a=input("Enter the string value:")
print(len(a))
for i in range(0,(len(a)),2):
    print(a[i])


word = input('Enter word ')
print("Original String:", word)
size = len(word)
print(size)
print("Printing only even index chars")
for i in range(0, size , 2):
    print("index[", i, "]", word[i])


word = input('Enter word ')
print("Original String:", word)
x = list(word)
for i in x[0::2]:
    print(i)

print("-------------------------------------------------")
'''

#Write a program to remove characters from a string starting from zero up to n and return a new string.
'''
a="chadura tech"
print(a[1:])

def remove_fc(word,n):
    print("enter the string",word)
    x=word[n:]
    return x
print(remove_fc('ashwin',1))
print(remove_fc('chadura',2))

'''
#Exercise 5: Check if the first and last number of a list is the same
'''
def firstandlast_samenumbert(list):
    print("give list:",list)
    if list[0]==list[-1]:
        return True
    else:
        return False  
print(firstandlast_samenumbert(list=(1,2,3,4,4,5,1)))
print(type(list))

def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

'''
#Exercise 6: Display numbers divisible by 5 from a list

'''def divisible(list):
    print("given list:",list)
    for i in list:
        if i%5==0:
           return (i)
print(divisible(list=[5,10,2,25,23,45,65,38]))  
'''
'''
list=[5,10,2,25,23,45,65,38]
#print("given list:",list)
for i in range(0,len(list)):
        if list[i]%5==0:
           print(list[i])'''
#Exercise 7: Return the count of a given substring from a string
'''
string='chadura tech previate limit chadura'
print(string.find("chadura",2))
print(string.count("chadura"))


def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'      #@ \\\\\\\\\\\\\\///////////////////
    return count
count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")

'''
#Exercise 8: Print the following pattern
'''
for i in range(0,6):
    for j in range(i):
        print(i,end="")
    print("\n")     
'''
'''
a=[131]
b=a[::-1]
print(b)
if a==b:
    print('Yes. given number is palindrome number',a)
else:
    print("No. given number is not palindrome number")   

''''''
def merge_list(list1, list2):
    result_list = []
    
    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to result list
            result_list.append(num)
    
    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            # add even number to result list
            result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))


'''
#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
'''
number = 7530
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")


num = int(input("Enter an integer: "))
while num > 0:
    digit = num % 10
    print(digit, end=" ")
    num //= 10
'''    
#Exercise 12: Calculate income tax for the given income by adhering to the rules below   
'''
income = 20010
tax_payable = 0
print("Given income", income)
if income<=10000:
    tax_payable = 0
elif income<=20000:
    x=income-10000
    tax_payable=x*10/100
else:
     tax_payable = 0
     tax_payable = 10000 * 10 / 100   
     tax_payable+=(income-20000)*20/100
print("Total tax to pay is", tax_payable)
'''
#Exercise 13: Print multiplication table from 1 to 10
'''
for i in range(1,11,1):
    print(i,end="\t",)
print(" ")    
for i in range(2,21,2):
    print(i,end="\t")
print(" ")    

for i in range(3,31,3):
    print(i,end="\t")
print(" ")    

for i in range(4,41,4):
    print(i,end="\t")
print(" ")

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print(" ")
'''    
#Exercise 14: Print a downward Half-Pyramid Pattern of Star
'''
for i in range(6,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print(" ")  
'''

#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp
'''
def expertion(base,exponent):
     c=base**exponent
     return c

print(expertion(base=3,exponent=abs(int(3)))) 
#x=expertion(base=3,exponent=abs(int(3)))
#print(x)
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base   # recursive function
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(3, 3)

'''




