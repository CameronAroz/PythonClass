#Python Class 2:

# Review::
#1. git init the directory
#2. git status to make sure everything is working correctly
#3. git add <filename>: had to add the file
#4. git commit -m "Comments"
#   Comments the changes that you made
#5. git log



#Python Class 3:

##Python Counting
#Arrays have starting positions at 0

##Variable Declaration
person_name = "Courtney"
favorite_number = 21
gender = "her"

##Type of Object: Tuple
#Creating a variable, person, and assigning three traits to it
person = (person_name, favorite_number, gender)
##Can access elements in an array through indexing
#person[0] -> references person_name. 
print person[0]
print person[1]
print person[2]

##Populates the {} with the variable that is above
print "Howdy"
print "my name is {}".format(person_name)
print "my favorite number is {}".format(favorite_number)

#List all the things I have my favorite number of
print "{} has {} books in {} collection".format(person[0],person[1],person[2])
print "{} has seen {} of {} favorite movies".format(person[0],person[1],person[2])
print "{} has {} pairs of socks in {} drawer.".format(person[0],person[1],person[2])

