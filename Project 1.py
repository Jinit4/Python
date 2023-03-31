# To make a calculator in python 
# Should perform following functions 
# Add, Subtract, Multiply, DIvide and Modulus(gives remainder)
# Lets take input from user 
a = input("Enter the value of a : ")
b = input("Enter the value of b : ")
a = int(a)
b = int(b) 
print (" 1) Addition ")
print (" 2) Subtraction ")
print (" 3) Multiplication")
print (" 4) Division")
print (" 5) Modulus")
o = input ("Select the number operation to be done : ")
o = int(o)
if o == 1:
    Sum = a+b
    print (Sum)
elif o == 2:
    Subtraction = a-b
    print (Subtraction)
elif o == 3:
    Multiplication = a*b
    print (Multiplication)
elif o == 4:
    Division = a/b
    print (Division)
elif o == 5:
    Modulus = a%b
    print (Modulus)
else :
    print ("Invalid Number entered")