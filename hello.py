###Python Class 3:
#Tuples
#Variable Declarations
#Lists: Similar to a Tuple

##Accessing the specific "sys" library
from sys import argv

#Note to self: argv gets us the [program_name, name, number, gender]


##Variable Declaration
program_name = argv[0]
person_name = argv[1]
favorite_number = argv[2]
gender = argv[3]

##Type of Object: Tuple
#Creating a variable, person, and assigning three traits to it
#Cannot change a tuple unless make a copy of it
#Cannot change an individual element of a tuple
person = (person_name, favorite_number, gender)


#**SHORTCUT**#
#Assigns Variables All at Once Instead of One at a Time
new_name, new_number, new_gender = ('Paul',16,'his')
andrew = ('Andrew',6,'his')
courtney = ('Courtney',21,'her')

##Reassigned the variable person to be andrew
person = andrew
##Can access elements in a tuple through indexing
#person[0] -> references person_name. 

##Populates the {} with the variable that is above
print "Howdy"
print "my name is {}".format(person[0])
print "my favorite number is {}".format(person[1])

#List all the things I have my favorite number of
print "{} has {} books in {} collection".format(person[0],person[1],person[2])
print "{} has seen {} of {} favorite movies".format(person[0],person[1],person[2])
print "{} has {} pairs of socks in {} drawer.".format(person[0],person[1],person[2])

