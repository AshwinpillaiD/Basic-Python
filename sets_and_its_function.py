
name={"ashwin",1,2.5,"ashwin","win"}
print(name) # don't allow duplicate element to print
print(type(name))

for name1 in name:   # Access Values Using For loop
    print(name1)

name.add(15)
print(name)    # Adding New Element
b={"raj",'niro',"hari","shyam"}
name.update(b)
print(name)
name.remove('ashwin')
print(name)
name.discard('raj')
print(name)

name.pop()
print(name)
name.clear()
print(name)
del name
#print(name)


a={1,2.5,"ashwin","win"}
b={"raj",'niro',"hari","shyam"}
c=a.union(b)
print(c)
a.update(b)
print(a)


a={1,2,3,4,5,6}
b={6,7,8,9,10}
c=a.intersection(b)
print(c)
a.intersection_update(c)
print(a)

a={1,2,3,4,5,6}
b={6,7,8,9,10}
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)


a = {5,6,7}
b = {5,6,7}
c=a.isdisjoint(b)
print(c)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)
