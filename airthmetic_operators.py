
# These are basic types of Airthmetic Operations which are +, -, /, % and * 
age1 = 2
age2 = 8
age = age1 + age2
print(age)
agee = age1 - age2
print (agee)
ae = age1*age2
print (ae)
ageee = age2//age1 # decimal later portion is removed in case output is 2.5 then output will be just 2
print (ageee)
a = age2 % age1 #This prints the remainder after division is performed
print (a)
print(5 ** 2) #this will print the power i.e here 5 square 
# # Lets look at changing a variable value and then printing the new value
# old_age = input("Enter your Old Age: ") #Here the age will be considered as a string when it will be taken as an input
# #So we convert it to int type
# int(old_age) # We add this line so that it sknows that the input obtained is of type integer
# new_age = int(old_age) + 2
# print(f"Your current age is {new_age}")

#we can also convert the valid values into float() str() bool()
#FLoat, String, Boolean
number = 18
print(float(18))

#Print sum of 2 Numbers

first = input("Enter the first number : ")
second = input("Enter the second number : ")
Sum = int(first) + int(second) #Here we need to convert to int in the same line where we are adding two numbers else the input will be considered as string
print(f"The sum of two numbers {first} and  {second} is  {Sum}")

#Shortcuts

i = 5
print (i)
i = i+2 # Here the value of i will be reassigned to i = i + 2 as previously i = 5 Here value of i will be 7
i += 2 # This means the same thing i = i + 2 here I will change its value to 9
print (i)
#Similarly
i -= 2 # This will give output i = i-2
i *= 2 # This will give output i = i*2


# Operator Precedence
result = 2 + 3 * 5  # There will be a detailed operator precedence chart refer the same for precedence of operations


#comparision operator
print (3>2) # >,<,>=,<=, == greater than less than , greater than equal to , less than equal to, equal to 3 == 2, not equal to != 

#logical operartor
#OR operator 
# If atleast one of the coni=dition is true than it will print true else returns false
print (2>3 or 3<4)

#And Operator
#If both the conditions are true then it will return true else returns false
print (2<3 and 3>2)

#Not Operator
#makes the output reverse like if we are getting true not will reverse it to false
print (not 3>2)