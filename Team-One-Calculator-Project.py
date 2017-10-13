# FILE NAME : Team-One-Calculator-Project.py
# DESCRIPTION : Calculator Program
# FUNCTION DEFINITIONS:

def div(n1,n2):
 return (n1/n2)

def mult(n1,n2):
 return (n1*n2)

def sub(n1, n2):
 return (n1-n2)

def add(num1,num2):
	return (num1+num2)	

# INITIAL MESSAGE:
print ("Welcome to Calculator Function")
print ("Menu:")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Division")
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if (choice == '1'):
   print(num1,"+",num2,"=", add(num1,num2))

elif (choice == '2'):
   print(num1,"-",num2,"=", sub(num1,num2))

elif (choice == '3'):
   print(num1,"*",num2,"=", mult(num1,num2))

elif (choice == '4'):
   print(num1,"/",num2,"=", div(num1,num2))
else:
   print("Invalid input")
