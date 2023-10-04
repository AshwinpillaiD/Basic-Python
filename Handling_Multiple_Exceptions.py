 
try:
    a=10/20
    print(a)
    b=[10,20,30,40]
    print(b[10])
except ZeroDivisionError:
    print("denominator cant be zero")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print(e)
 