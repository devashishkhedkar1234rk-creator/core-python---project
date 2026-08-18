
# Basic Variables
'''''
s_name="Devashish"
age=21
percentage=95.5
placed=True

print("Student Name",s_name, type(s_name))
print("Age",age,type(age))
print("Percentage",percentage,type(percentage))
print("Placed",placed,type(placed))

# Type Conversion

age=input("Enter your age:")
age=int(age)
future_age= age+5
print("Your age after 5 years is:",future_age)

#Built-in Functions

numbers=[30,50,10,90,70]
minimum=min(numbers)
maximum=max(numbers)
total=sum(numbers)

print("Values",numbers)
print("Minimum" ,minimum)
print("Maximum",maximum)
print("Total",total)

#Numeric Data Types

num_int=200
num_float=30.50
num_complex=10+5j

print("Integer:",num_int)
print("Type:",type(num_int))
print("Float:",num_float)
print("Type:",type(num_float))
print("Complex:",num_complex)
print("Type:",type(num_complex))

# Length and Absolute Value

full_name="Devashish khedkar"

name_length=len(full_name)

print("Fulln Name:",full_name)
print("Length of name:", name_length)

number=-45.6

print("Number:",number)
print("Absolute Value:",abs(number))

# Round Function
number=79.4567
print(round(number,2))

#Power Function

number=int(input("Enter number"))
print("Square", pow(number,2))
print("Cube",pow(number,3))
'''''

#Arithmetic Operators
'''''
a=int(input("Enter First Number"))
b=int(input("Enter second Number"))

print("Addition:",a+b)
print("Subtraction",a-b)
print("Multiplication:",a*b)
print("Division",a/b)
print("Floor Division",a//b)
print("Modulus",a%b)
print("Power",a**b)

'''''
# Comparison Operators
'''''
a= int(input("Enter First Number:"))
b=int(input("Enter Second Number"))

print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
'''''
# Logical Operators
'''''
age=int(input("Enter age"))
percentage= float (input("Enter percentage:"))
result=age>=18 and percentage >=60
print(result)

'''''
# ASsignment operators
''''
x=100
x+=20
x-=10
x*=2
x/=5
print(x)

'''''
# Simple Eligbility Check
'''''
marks=float(input("Enter marks:"))
if marks>=60:
    print("Eligible")
else:
    print("Not Eligible")

'''''
#Even or odd
'''''
number=int(input("Enter number:"))
if number %2==0:
    print("Even")
else:
    print("Odd")

'''''
#String Indexing
''''
text="DevashishKhedkar"

print("First",text[0])
print("Last",text[-1])
print("Fifth",text[4])
print("Length",len(text))

#String Slicing

print(text[0:6])
print(text[-4:])
print(text[::-1])
'''''