'''sampleList = [10, 20, 30, 40]
del sampleList
print(sampleList)'''

'''
aList = ['a', 'b', 'c', 'd']
newList = list(aList)
if aList is newList:
    print("true")
else:
    print("flase")
'''
'''l = [] * 10
print(len(l))
print(l)
'''
'''
aList = [5, 10, 15, 25]
print(aList[::-2])
'''

'''aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [2 * x for x in aList]
print(pow2)
'''
'''
list1 =['a_z','ashwin']
print (max(list1))
print (min(list1))
'''



# calculate file size in KB, MB, GB
def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

path = pathlib.Path(r'/home/transit/Documents/practice/constant.py')
f_size = path.stat().st_size
print('File size in bytes', f_size)

# you can skip this if you don't want file size in KB or MB
x = convert_bytes(f_size)
print('file size is', x)
