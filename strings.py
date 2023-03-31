
sent1 =  "Today was a Beautiful day"
firstName="Jinit"
lastName="Desai"
name = firstName + " " + lastName #here we are performing string concatenation where we join two strings 
print (name)
excited = "Hi " * 10 # We can multiply a string 
print (excited)

sentence = "Jinit Desai is here"
# every charater in python is assigned an index
print(sentence [0]) #slicing the string

print (sentence[0:5]) # when we take the slicing python doesnt count the last word so in 0 to 5 it will be 0 to 4 
#which is 5 characters 
print (sentence[0:8:3])
print ([sentence[-2]])
print ([sentence[:-2]]) #Semicolon and -2 will print all the elements from 0 to -2 -2 not included

name = "Jinit Desai"
print(name) #The original string doesnot change while we apply method 
# When we type name. we will see a list of methods. We can make a lot of changes in that string
print(name.upper()) # This method will help us to make everything in capital
print(name)

#Next method we will be looking at is find if we want to find anything in the string than we can use it 
print (name.find("J")) # Here we get the index of that character or the string in that variable
#if we do not get the desired value in that variable then it will return -1
print (name.find("es")) # this will give the starting index of that word in the varibale above

# next we will be looking at replacing the value in the variable
print(name.replace("Desai", "Iron Man"))
#this wont change the initial  String variable name
print(name)

print ("j" in name ) #This will find if a character or a string exists in the name and will return the Boolean value
print ("Desai" in name) # will print true