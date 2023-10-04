a=[1,2,3,4,5,6,7]
print(a)
print(type(a))
a[1]=22
print(a)

# slicing
# getting value by index

print(a[6])
print(a[-1])
print(a[2:])
print(a[:3])
print(a[0:4])
print(a[:4])
# :: used to print getting index value only
print(a[1::6])
print("----------------------------------------------------")

b=[1,True,'ram',2.5]
print(b)
print(b[3])
print(b[3],"type is",type(b[3]))
print(b[2],"type is",type(b[2]))
print(b[0],"type is",type(b[0]))

print("----------------------------------------------------")

a=[1,2,3,4,[11,22,33,44,55],5,6,7,8]
print(a[4][2])


print("----------------------------------------------------")

a=[11,22,33,44,55,66,77,88]
print(a)
a.clear()
print(a)
a=[11,22,33,44,55,66,77,88]
b=a.copy()
print(b)
a=[11,99,33,99,55,66,77,88,99]
print(a.count(99)) 
print(a.index(99)) #find the index of value
print(len(a))

 # a='11,99,33,99,55,66,77,88'
 # print(len(a))

print(max(a))
print(min(a))
a.pop(3)  # remove Element using index
print(a)
a.remove(99) # Remove first occurrence of value.
print(a)

print("----------------------------------------------------")

names=['ashwin']
names.append('raj')
names.append('shyam')
print(names.append('gowtham'))
print(names)
name2 = ["asdfg",'qwer']
names.extend(name2)
print(names)
names.insert(0,"Suriya")
names.insert(1,"saran")
print(names)

print("-----------------------------")
print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,5,2)))

print(list("rajkumar")) # list expected at most 1 argument

a=[10,50,100,25,85]
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.sort(reverse=True)
print(a)
a.sort(reverse=False)
print(a)


a=["Orange","Apple","Zebra"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a=["Orange","apple","Zebra"]
a.sort(key=len)
print(a)



