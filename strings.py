
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