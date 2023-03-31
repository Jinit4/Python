# There are different types of variables such as String Integer Float Boolean 
# In Python we do not need to define the variable type and we can directly give the value and variable 
# type will be detected automatically
age = 23
print(age)

sentence ="Jinit is here"
print(sentence)

name,age ="Jinit",23
print(name,age)
# the variable having values once defined can change their values if the variable is defined again
name = "Desai"
age = 24
print (name, age)
 
# Boolean values let us know if the value is Treu or False
#is_adult = true This will give an error as python is case sensitive 
is_adult = True 

firstName = "Tony"
lastName="Stark"
age = 51
is_genius = True

print (firstName + lastName)
print (f"Age of  {firstName}  {lastName}  is  {age}")
print (f"Tony is Genius  {is_genius}") 

# taking input from user

name = input("What is your Name? ")
print("Hello " +name) # String concatenation
