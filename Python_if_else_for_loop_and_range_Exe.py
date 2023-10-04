
#Exercise 1: Print First 10 natural numbers using while loop
'''
i=1
while i<=10:
    print(i)
    i+=1    
'''
#Exercise 2: Print the following pattern
'''
for i in range(1,6):
    for j in range(1,i+1):    # range (start,end-1,step)
        print(j ,end="")
    print("")    
'''
#Exercise 3: Calculate the sum of all numbers from 1 to a given number
'''
a=[]
while True: 
    b=int(input("Enter the integer value :"))
    a.append(b)
    print(a)
    print(sum(a))
    
else :
    print("complete") 
   

'''
"""
n=2
for i in range(1,11,1):
    c=n*i
    print(c)
"""
'''
#Exercise 5: Display numbers from a list using loop

num =[23,25,46,55,67,65,987,676]
for numi in num:
    if numi > 500:
        break
    elif numi > 150:
        continue
    elif numi%5==0:
     print(numi)        
     
'''
#Exercise 6: Count the total number of digits in a number
'''
n=str(25434)
print(len(n))
count=0
while n!=0:
    n//=10
    count+=1
print(count)
'''
#Exercise 7: Print the following pattern
'''
n = 5  # Set the number of rows

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
'''

#Exercise 8: Print list in reverse order using a loop
'''
list1 = [10, 20, 30, 40, 50]
list1.sort(reverse=True)
print(list1)
for list in list1:
    print(list)


list1 = [10, 20, 30, 40, 50]
newlist=reversed(list1)
for item in newlist:
    print(item)

'''

#Exercise 9: Display numbers from -10 to -1 using for loop
'''
for i in range(-10,0,1):
    print(i)
'''
#Exercise 10: Use else block to display a message “Done” after successful execution of for loop
'''
for i in range(5):
    print(i)
else:
    print("done")    

'''
#Exercise 11: Write a program to display all prime numbers within a range
'''
for num in range(25,51,1):
    if num >1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)


'''

#Exercise 12: Display Fibonacci series up to 10 terms
'''
a,b=0,1
for i in range(10):
    print(a,end=" ")
    res=a+b

    a=b
    b=res
 '''
#Exercise 13: Find the factorial of a given number
'''
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)
'''
#Exercise 15: Use a loop to display elements from a given list present at odd index positions
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i)

'''
#Exercise 16: Calculate the cube of all numbers from 1 to a given number
'''
num=int(input("Enter the value:"))
for i in range(1,num+1):
    c=i**3                #formet srting
   
    print(f"Current Number is : {i} and the cube is {c}")

'''
#Exercise 17: Find the sum of the series upto n terms
'''
lis=[]
for ritem in range(5):
    lis1=int(input("enter the value:"))
    lis.append(lis1)
sum=sum(lis)
print(sum)
'''
'''
n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)

'''
#Exercise 18: Print the following pattern
'''
for i in range(1,6):
    print(i*" * ")
for j in range(4,0,-1):
    print(j*" * ")   


rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

'''
