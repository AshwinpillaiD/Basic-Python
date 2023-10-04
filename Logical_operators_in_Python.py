# Logical Operators in Python
"""
and
or
not

"""

a="ashwin"
b="ashwin"
c="pillai"

print('a\n b\n c')
print( a<b and c==a )
print( a>=b and c!=a )
print( a==b and c==a )
print( a!=b and c!=a )
print(id(a))
print(id(b))
print(id(c))

e="123"
f="123"
d="546"
print(id(e))
print(id(f))
print(id(d))
print( e<f and d==e )
print( e>=f and d!=e )
print( e==f and d==e )
print( e!=f and d!=e )



print('-----------------------------------------')

a="ashwin"
b="ashwin"
c="pillai"

print('a\n b\n c')
print( a<b or c==a )
print( a>=b or c!=a )
print( a==b or c==a )
print( a!=b or c!=a )
print(id(a))
print(id(b))
print(id(c))

print('-----------------------------------------')

a="ashwin"
b="ashwin"
c="pillai"

print('a\n b\n c')
print(not( a<b or c==a ))
print(not(a>=b or c!=a ))
print(not(a==b or c==a ))
print(not(a!=b or c!=a ))
print(id(a))
print(id(b))
print(id(c))