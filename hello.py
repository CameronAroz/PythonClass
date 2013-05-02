#Python Class 2:

#1. git init the directory
#2. git status to make sure everything is working correctly
#3. git add <filename>: had to add the file
#4. git commit -m "Comments"
#   Comments the changes that you made
#5. git log

##Variable Declaration
person_name = "Courtney"
favorite_number = 21
gender = "her"

##Populates the {} with the variable that is above
print "my name is {}".format(person_name)
print "my favorite number is {}".format(favorite_number)

#List all the things I have my favorite number of
print "{} has {} books in {} collection".format(person_name,favorite_number,gender)
print "{} has seen {} of {} favorite movies".format(person_name,favorite_number,gender)
print "{} has {} pairs of socks in {} drawer.".format(person_name,favorite_number,gender)

