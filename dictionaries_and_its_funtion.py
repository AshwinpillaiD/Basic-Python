win={"name":"ashwin", "age":22, "place":"klt"}
print(win)
print(type(win))
print(win["name"])
print(win.values())
print(win.keys())
print(id(win))
print(win.get('age'))
print(win.items())
print("place" in win.keys())
for a in win:
   print(a)

print('-------------------------------------------------------')   
for x in win.values():
   print(x)

for a in win.items(): # this statement  output is tuple 
   print(a)

for a,b in win.items():
   print(a,b)

if "age" in win:
    print("present")   

print('-------------------------------------------------------')   

win.update({"phone":123456789})
print(win)
win["age"]=70
print(win)
win.pop("age")
print(win)
win.clear()
print(win)
del win
#print(win)

print('-------------------------------------------------------')   
#  nested dictionaries statement
wins={
 "ash":
        {"name":"ashwin","age":22,"place":"klt"},
 "ash2":{ "name":"ashwin","age":45,"place":"klt"}
    
}
print(wins)
print(wins["ash"])
print(wins["ash2"])
print(wins["ash"]["age"])
print(wins["ash2"]["age"])

