#in-built functions
#FUnctions wich already exist in python 
int()
str()
bool()

#Module functions
import math 
#Math module has many functions 
print(dir(math)) #this will help to print all the math fi=unctions which can be used 

#If we want to take a certain(specific) function from a module we will type
from math import sqrt
print (sqrt(16)) 
#if we want to gt all the functions we type
from math import *

#user defined function 
#Syntax for defining a function in python
#def funtion_name(parameters):
    #//do something
def print_sum(first,second):
    print (first+second)

print_sum(1,2)

def print_sum(first,second = 4): # Here we can pass the default value if no value is passed 
    print (first+second)

print_sum(1)

