
i=1
while i<=10:
    print(i)
    i+=1   
print("---------------------------------------------")

i=9
while i<=10:
    print(i)
    i+=1
print("---------------------------------------------")


i=int(input("enter the value i:"))
n=int(input("enter the value n:"))
while i <= n: 
    print(i)
    i += 2

print("---------------------------------------------")

i=int(input("enter the value i:"))
n=int(input("enter the value n:"))
while i <= n:
    a=int(input('enter yhe value a:'))  
    b=int(input('enter yhe value b:'))
    c=a+b
    print("total :"+ str(c))
    i+=1   

print("---------------------------------------------")

while True:
    print("ashwin")

#NESTED WHILE LOOP

i=1
j=1
while i <= 6:
    j=1
    while j<=i:
        print("8",end=" ")  
        j+=1  
    print(" ")
    i+=1

print("---------------------------------------------")

i=1
j=1
while i<=5:
    print("hi")
    j=1
    while j<=5:
        print("hello",end=" ")
        j+=1
    i+=1