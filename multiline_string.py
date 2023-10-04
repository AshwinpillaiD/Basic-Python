#  three quotation marks use the paragraph statment
a="""
Lorem Ipsum is simply dummy text of the printing and typesetting industry.text  Lorem Ipsum has been the industry's standard dummy ever since the 1500s,
"""
print(type(a))
print(a)

print("-----------------------------------------------------------")
#  three quotation marks use the paragraph statment
a='''  The program defines a string variable a containing a multi-line text string. The data type of the variable a is str. The program then uses the print function to display the data type of a, which is str, and the value of a which is the text string itself.

The above program is a Python script that takes multi-line input from the user in the form of a paragraph.'''
print(type(a))
print(a)

print('-----------------------------------------------------------')
#  single and duble quotation marks use the paragraph statment
a=("Lorem Ipsum has been the industry's standard dummy")
print(type(a))
print(a)

print('-----------------------------------------------------------')
#  single and duble quotation marks use the paragraph statment
a=('Lorem Ipsum has been the industry"s standard dummy')
print(type(a))
print(a)
 
print("-----------------------------------------------------------") 

para=[]
print("enter a para:")

while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)







