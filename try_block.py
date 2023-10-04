#try block 

try:
    a=10/0
except  Exception as e:
    print(e)  

print("------------------------------------")
# try else block
try:
    a=10/20
  #  b=10/0
except  Exception as e:
    print(e)  
else:
    print("Value:",a)
  #  print("Value:",b)   
       
print("------------------------------------")

try:
  #  a=10/20
   b=10/0
except  Exception as e:
    print(e)  
else:
   # print("Value:",a)
   print("Value:",b) 
finally:
    print("complete")  

print("------------------------------------")
