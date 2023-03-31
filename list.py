marks =[95, 98, "maths"] # In list we can store variables of different data types 
print (marks)
# now if we want to print individual items from list then
print (marks[0]) # Here we write the index number the indexing in python can be positive negative and it starts from 0
print (marks[-1]) # Here we get the output from behind when we give a negative value
print (marks [0:2])# Here we can print a range of values the genral notation is list[start, stop index] where the stop index is not included

#Using for loop 
for score in marks:
    print (score)

#Operarations that can be performed in the list 
#Append operation which means to Join

marks.append(99) #Append takes only one value and adds the value in the end 
print(marks)

#insert operation 
marks.insert(0, 56) #Insert can be used to insert value at a certain position in a list insert (index, value)
print (marks)

#to check if a value is present in a list 
print ("maths" in marks)
print (56 in marks)

#Length of the list 
print(len(marks))

#Lets iterate list using while loop
i=0
while i < len(marks): # Here we print the same list usig while loop
    print (marks[i])
    i=i+1

#if we want to clear the list 
marks.clear() #this will help us to clear the whole list
print (marks)
