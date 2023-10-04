a=['23','45','76','89','9']
b=['43','56','78','98','6']
print(a[3])

print(type(a))
a.append(str(10))
print(a)
a.extend(b)
print(a)

print('|'.join(a))
print(type('|'.join(a)))

print(a)
