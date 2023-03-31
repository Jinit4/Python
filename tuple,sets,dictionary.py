#Tuple is similar to the list the only thing is tupe is immutable 
#Once a tuple is defined it cannot be changed 
# We saw in the list we could append add and make various changes in the list once it is made but in the tuple it wont be possible 
marks =(95,98,99,98,97,99) # Tuple will be defined using () and list is defined using []
#marks[0] = 87 #This will give us an error that tuple object does not support item assignment

# We can count the elements in the tuple
print(marks.count(99))

# We can also get the index of the element in the tuple 
print(marks.index(99)) #The index value will be printed for when the element first appears

#sets
#Sets are used when we want to store unique elements
marks = {95,98,97,98,97}
print (marks) #Here we cannot print (marks[0]) because in sets index does not exsist
#Sets can be defined using { } or can be simply defined like
greeting = "hey", "hello", "hi" # This is still considered to be a set
print (greeting)
#sets are considered as unordered as there is no index 

#Dictionary
#Dictionary stored the elements in a Key Value Pair
report = {"English": 65, "Chemistry": 87}
print (report["Chemistry"])

report["physics"] = 88; #Adding new subject and its marks
print(report)

#We can also change marks for exsisting subject in the dictionary
report["physics"] = 99;
print(report)