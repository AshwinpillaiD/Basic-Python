for i in range(6):
    for j in range(i):
        print("*",end="")
    print(" ")   # this statement print new line 

print("-------------------------------------")

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print(" ")
    
print("-------------------------------------")

for i in range(65,91): #ASCII CHARATER  A-Z => 65-90  
    print(chr(i))
for i in range(97,123): #ASCII CHARATER  a-z=> 97-122
    print(chr(i))
