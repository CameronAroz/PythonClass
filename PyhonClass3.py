##Python Class 3
#http://docs.python.org/2.7 //Use for questions

###REVIEW FROM HOMEWORK:
##To change a string into an integer
#int("12")
##To change aninteger into a string
#str(3
##Python is Case Sensitive


##Substitution in Strings
#print "I have {} cars".format(3)
##Output: I have 3 cars

##Out of order!: The numbers represent the indexes of what you input into "format"
#print "I'd like to order {1} slices of pizza, on a {2} crust please! And hold the {0}".format(pizza[0],pizza[1],pizza[2])

##More descriptive variable names so people can follow your code

#CTRL + d // Creates duplicates

teacher_names = ['andrew','bobby','esther']

###Creating a For Loop:
##Need to insert 4 spaces to include the loop
##Indentation Matters
##teacher_name variable, in for loop is a GLOBAL variable
##prints all elements in the list
for teacher_name in teacher_names:
	python_sentence = "{} loves Python! Whoo!".format(teacher_name)
	print python_sentence
##Assigns teacher_name = Esther	
print teacher_name


##Prints the range from 0-19 in a list
#Can specify an interval and the steps
#range(start,end,step)
print range(20)


###Prints "I love pizza" 2 times
for iteration in range(2):
	print "Loop " + str(iteration) + ": I love pizza"
	print "Loop {}: I love pizza".format(iteration)
	
##Returns True/False concerning whether or not something is in the list
#'boolean' is a data type that only represents: True or False //Not a String
print 'andrew' in teachers_name
print 'andrew' not in teachers name


	
	



