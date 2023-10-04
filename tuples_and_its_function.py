
a=(1,"ashwin",2.4,"appu")
b=("ash") # any single value without camaa(,) consider us value type only
c=("ash",) # this statement with camaa(,) type is tuple 
print(a)
print(type(a))
print(type(b))
print(type(c))
print(a[1])
print(a[1:3])
print(a[:-1])
print(a[-1])
print(a[-1:]) # this statement print the tuple value with (,)

b=list(a)
print(type(b))

b.append("win")
print(b)
a=tuple(b)
print(a)
print(type(a))

for i in a:
    if i==2.4:
     continue
    print(i)
print("")

print("-----------------------------------------------------------------------")
a=(1,"ashwin",2.4,"appu")
print(len(a))
#del a
#print(a)

print("-----------------------------------------------------------------------")
a=(1,"ashwin",2.4,"appu")
b=(2,'ashwin',3.4,'appu')
c=a+b
print(c)
print(c[4])
d=(a,b)
print(d)
print(d[1])
print(d[1][1])
x=('ashwin',)*5
print(x)

print("-----------------------------------------------------------------------")

a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
print(min(a))
print(max(a))








